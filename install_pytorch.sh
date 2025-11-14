#!/bin/bash

# Install PyTorch with GPU support after pipenv install
# This script installs PyTorch with CUDA support

echo "========================================="
echo "  PyTorch GPU Installation Helper"
echo "========================================="
echo ""

# Check if pipenv is installed
if ! command -v pipenv &> /dev/null; then
    echo "ERROR: pipenv not found!"
    echo "Please install pipenv first: pip install pipenv"
    exit 1
fi

echo "Step 1: Checking current PyTorch installation..."
echo ""

pipenv run python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}')" 2>/dev/null || echo "PyTorch not installed"

echo ""
echo "========================================="
echo ""
echo "Select PyTorch installation option:"
echo "  1. CUDA 11.8 (Most compatible)"
echo "  2. CUDA 12.1 (Latest)"
echo "  3. CPU only (No GPU)"
echo "  4. Skip (already installed)"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "Installing PyTorch with CUDA 11.8..."
        pipenv run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
        ;;
    2)
        echo ""
        echo "Installing PyTorch with CUDA 12.1..."
        pipenv run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
        ;;
    3)
        echo ""
        echo "Installing PyTorch CPU version..."
        pipenv run pip install torch torchvision torchaudio
        ;;
    4)
        echo ""
        echo "Skipping PyTorch installation..."
        exit 0
        ;;
    *)
        echo "Invalid choice!"
        exit 1
        ;;
esac

echo ""
echo "========================================="
echo "  Verifying Installation"
echo "========================================="
echo ""

pipenv run python -c "import torch; print(f'PyTorch Version: {torch.__version__}'); print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'CUDA Version: {torch.version.cuda if torch.cuda.is_available() else \"N/A\"}'); print(f'Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"CPU\"}')"

echo ""
echo "========================================="
echo ""
echo "Installation complete!"
echo ""
echo "To use the application:"
echo "  1. Run: pipenv shell"
echo "  2. Run: streamlit run app.py"
echo ""
