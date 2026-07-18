import torch
import sys

def main():
    print("=" * 50)
    print("      TESLA AI TRACK: PYTORCH ENVIRONMENT CHECK      ")
    print("=" * 50)
    
    # 1. Check Python and PyTorch Core Versions
    print(f"Python Version : {sys.version.split()[0]}")
    print(f"PyTorch Version: {torch.__version__}")
    
    # 2. Hardware Acceleration Check
    # cuda.is_available() checks if you have an NVIDIA GPU and proper drivers installed
    gpu_available = torch.cuda.is_available()
    print(f"GPU Acceleration Available: {gpu_available}")
    
    if gpu_available:
        # Fetch metadata about your graphics processing hardware
        current_device = torch.cuda.current_device()
        gpu_name = torch.cuda.get_device_name(current_device)
        print(f"Active GPU Device Name    : {gpu_name}")
        
        # Target the GPU explicitly
        device = torch.device("cuda")
        print("\n[SUCCESS] Matrix operations will execute on your GPU hardware.")
    else:
        # Default to standard central processing unit
        device = torch.device("cpu")
        print("\n[NOTICE] Running on CPU. (No NVIDIA CUDA GPU detected or configured).")
        print("Note: For basic learning, a CPU works perfectly fine!")

    print("-" * 50)
    
    # 3. Simple Matrix Operation Test (The math behind neural networks)
    # Create two random 3x3 matrices directly on your selected hardware device
    matrix_a = torch.rand(3, 3, device=device)
    matrix_b = torch.rand(3, 3, device=device)
    
    # Perform a matrix multiplication operation
    result = torch.matmul(matrix_a, matrix_b)
    
    print("Sample Matrix Multiplication Test Result:")
    print(result)
    print("=" * 50)

if __name__ == "__main__":
    main()
