import torch
print(f"PyTorch 版本: {torch.__version__}")
print(f"CUDA 是否可用: {torch.cuda.is_available()}")
print(f"CUDA 版本: {torch.version.cuda if torch.cuda.is_available() else '不可用'}")
print(f"GPU 數量: {torch.cuda.device_count()}")
if torch.cuda.is_available():
    print(f"當前 GPU: {torch.cuda.current_device()}")
    print(f"GPU 名稱: {torch.cuda.get_device_name(0)}")
    print(f"GPU 內存分配: {torch.cuda.memory_allocated(0) / 1024**2:.2f} MB")
    print(f"GPU 內存緩存: {torch.cuda.memory_reserved(0) / 1024**2:.2f} MB")