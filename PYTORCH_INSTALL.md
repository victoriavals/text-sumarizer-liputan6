# PyTorch GPU Installation Guide

## Problem
Pipenv tidak bisa resolve PyTorch dengan CUDA dependencies karena versi spesifik tidak tersedia di PyPI index.

## Solution

### Opsi 1: Install PyTorch Manual (RECOMMENDED)

**Setelah `pipenv install`, install PyTorch dengan GPU support secara manual:**

#### Untuk CUDA 11.8:
```bash
# Activate pipenv shell
pipenv shell

# Install PyTorch dengan CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Untuk CUDA 12.1:
```bash
# Activate pipenv shell
pipenv shell

# Install PyTorch dengan CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### Untuk CPU only:
```bash
# Activate pipenv shell
pipenv shell

# Install PyTorch CPU
pip install torch torchvision torchaudio
```

### Opsi 2: Skip Pipenv, Gunakan requirements.txt

```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install from requirements.txt
pip install -r requirements.txt

# Install PyTorch with GPU
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Opsi 3: Gunakan Conda (Alternative)

```bash
# Create conda environment
conda create -n liputan6 python=3.13

# Activate
conda activate liputan6

# Install PyTorch with CUDA
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Install other dependencies
pip install -r requirements.txt
```

## Verification

Setelah install, verifikasi PyTorch terinstall dengan benar:

```bash
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'CUDA Version: {torch.version.cuda if torch.cuda.is_available() else \"N/A\"}')"
```

Expected output:
```
PyTorch: 2.x.x+cu118 (atau cu121)
CUDA Available: True
CUDA Version: 11.8 (atau 12.1)
```

## Current Pipfile Configuration

Pipfile sekarang menggunakan PyTorch versi terbaru dari PyPI (CPU version) untuk kompatibilitas dengan pipenv. 

**Untuk GPU support, install manual setelah `pipenv install`.**

## Quick Start Commands

### Full Installation Steps:

```bash
# 1. Install dependencies via pipenv
pipenv install

# 2. Activate pipenv shell
pipenv shell

# 3. Install PyTorch with GPU (pilih sesuai CUDA version)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 4. Verify installation
python -c "import torch; print(torch.cuda.is_available())"

# 5. Run app
streamlit run app.py
```

## Why This Happens?

1. **PyTorch dengan CUDA** tidak tersedia di PyPI index standard
2. **Pipenv** kesulitan resolve dependencies dari multiple indexes
3. **Versi spesifik** (seperti 2.5.1+cu118) mungkin tidak exist atau sudah deprecated

## Recommended Workflow

Untuk development dan production:

1. ✅ Gunakan **requirements.txt** untuk dependency management
2. ✅ Install PyTorch manual dengan command dari pytorch.org
3. ✅ Document exact versions yang digunakan

Pipfile tetap berguna untuk:
- Package management non-PyTorch dependencies
- Lock file untuk reproducibility
- Virtual environment management

---

**Updated**: November 3, 2025
