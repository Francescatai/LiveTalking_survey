# CUDA Check

## 检查CUDA版本

```bash
nvcc --version
``` 

## 使用 Conda 安裝指定版本的 cudatoolkit
```bash
conda install cudatoolkit=11.3
``` 
## 確認虛擬環境使用的 cudatoolkit 版本
```bash
conda list cudatoolkit
``` 

## 現在使用環境(LiveTalking)
```bash
conda activate nerfstream-evelyn
``` 

## 現在使用環境(Ultralight-Digital-Human)
```bash
conda activate dh_evelyn
``` 

## 檢查CUDA是否可用
```bash
python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('CUDA version:', torch.version.cuda)"
``` 

## python內存監控
```bash
# 在另一個終端窗口執行
watch -n 1 'free -h; echo ""; ps -o pid,user,%mem,rss,command ax | grep python | grep -v grep'
``` 

## 檢查 CUDA 內存
```bash
watch -n 1 nvidia-smi
``` 

## 執行app.py
```bash
 (current)python app.py --model ultralight --avatar_id ultralight_avatar1 --transport webrtc --listenport 8011 --batch_size 2 --tts edgetts --fps 16 --W 320 --H 320 --max_session 1 --cuda_ray --data_range 0 10

CUDA_VISIBLE_DEVICES=0 python app.py --transport webrtc --model ultralight --avatar_id ultralight_avatar1 --batch_size 1 --preload 0 --W 160 --H 160 --cuda_ray --fp16

python app.py --model ultralight --avatar_id ultralight_avatar1 --transport webrtc --listenport 8010 --batch_size 2 --tts edgetts --fps 30 --W 320 --H 320 --max_session 1

python app.py --model ultralight --avatar_id ultralight_avatar1 --transport webrtc --listenport 8010 --batch_size 2 --tts edgetts --fps 16 --W 320 --H 320 --max_session 1 --cuda_ray --data_range 0 50

CUDA_VISIBLE_DEVICES=1 ulimit -v 10000000 && python app.py --model ultralight --avatar_id ultralight_avatar1 --transport webrtc --listenport 8010 --batch_size 1 --tts edgetts --fps 8 --W 192 --H 192 --max_session 1 --data_range 0 10