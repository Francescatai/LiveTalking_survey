import time
import os
from basereal import BaseReal
from logger import logger
from openai import OpenAI

# 設置默認 API 密鑰，如果環境變量存在則使用環境變量
DEFAULT_API_KEY = ""

def llm_response(message, nerfreal:BaseReal):
    start = time.perf_counter()
    # 優先使用環境變量中的 API 密鑰，如果沒有則使用默認值
    api_key = os.environ.get("OPENAI_API_KEY", DEFAULT_API_KEY)
    
    client = OpenAI(
        api_key=api_key,
        # 填写DashScope SDK的base_url
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    end = time.perf_counter()
    logger.info(f"llm Time init: {end-start}s")
    
    # 如果 API 密鑰為空，則返回錯誤信息
    if not api_key:
        error_msg = "OpenAI API 密鑰未設置。請設置 OPENAI_API_KEY 環境變量或在代碼中提供密鑰。"
        nerfreal.put_msg_txt(error_msg)
        return error_msg
    
    # 原有的 LLM 處理邏輯
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                      {'role': 'user', 'content': message}],
            stream=True,
            # 通过以下设置，在流式输出的最后一行展示token使用信息
            stream_options={"include_usage": True}
        )
        result=""
        first = True
        for chunk in completion:
            if len(chunk.choices)>0:
                #print(chunk.choices[0].delta.content)
                if first:
                    end = time.perf_counter()
                    logger.info(f"llm Time to first chunk: {end-start}s")
                    first = False
                msg = chunk.choices[0].delta.content
                lastpos=0
                #msglist = re.split('[,.!;:，。！?]',msg)
                for i, char in enumerate(msg):
                    if char in ",.!;:，。！？：；" :
                        result = result+msg[lastpos:i+1]
                        lastpos = i+1
                        if len(result)>10:
                            logger.info(result)
                            nerfreal.put_msg_txt(result)
                            result=""
                result = result+msg[lastpos:]
        end = time.perf_counter()
        logger.info(f"llm Time to last chunk: {end-start}s")
        nerfreal.put_msg_txt(result)
        return result
    except Exception as e:
        error_msg = f"LLM 處理錯誤: {str(e)}"
        nerfreal.put_msg_txt(error_msg)
        return error_msg    