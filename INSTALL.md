# 📦 Installation Guide

Panduan lengkap instalasi dependencies untuk Liputan6 Text Summarizer project.

## 🔧 Prerequisites

- **Python 3.13** (atau Python 3.8+)
- **pip** (sudah termasuk dengan Python)
- **Git** (optional, untuk clone repository)

## 🚀 Installation Steps

### Opsi 1: Menggunakan Pipenv (Recommended untuk Development)

#### Step 1: Install Pipenv

```bash
# Install pipenv globally
pip install pipenv
```

#### Step 2: Clone Repository (jika belum)

```bash
git clone https://github.com/victoriavals/text-sumarizer-liputan6.git
cd text-sumarizer-liputan6
```

#### Step 3: Install Dependencies

```bash
# Install semua dependencies dari Pipfile (kecuali PyTorch GPU)
pipenv install
```

**Note**: Ini akan install semua dependencies **kecuali PyTorch dengan GPU support**.

#### Step 4: Install PyTorch dengan GPU Support

**PENTING**: PyTorch dengan CUDA harus diinstall secara manual.

**Windows:**
```bash
# Double-click atau run:
install_pytorch.bat

# Pilih opsi CUDA version Anda (11.8 atau 12.1)
```

**Linux/Mac:**
```bash
# Make executable dan run:
chmod +x install_pytorch.sh
./install_pytorch.sh

# Pilih opsi CUDA version Anda
```

**Manual (jika script tidak berfungsi):**
```bash
# Activate pipenv shell
pipenv shell

# Install PyTorch - Pilih salah satu:

# CUDA 11.8 (Most compatible)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1 (Latest)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# CPU only (No GPU)
pip install torch torchvision torchaudio
```

#### Step 5: Verify Installation

```bash
pipenv run python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA Available: {torch.cuda.is_available()}')"
```

Expected output:
```
PyTorch: 2.x.x+cu118 (atau cu121)
CUDA Available: True
```

---

### Opsi 2: Menggunakan pip + venv (Recommended untuk Deployment)

#### Step 1: Create Virtual Environment

```bash
# Create venv
python -m venv venv
```

#### Step 2: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
# Install from requirements.txt
pip install -r requirements.txt
```

#### Step 4: Install PyTorch

**Pilih sesuai CUDA version:**

```bash
# CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# CPU only
pip install torch torchvision torchaudio
```

#### Step 5: Verify

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

---

### Opsi 3: Menggunakan Conda (Alternative)

#### Step 1: Create Conda Environment

```bash
conda create -n liputan6 python=3.13
conda activate liputan6
```

#### Step 2: Install PyTorch with CUDA

```bash
# CUDA 11.8
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# CUDA 12.1
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

# CPU only
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

#### Step 3: Install Other Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Quick Start After Installation

### For Development (Jupyter Notebooks):

```bash
# Activate environment
pipenv shell  # atau: source venv/bin/activate

# Run Jupyter
jupyter lab
```

### For Streamlit App:

```bash
# Activate environment
pipenv shell  # atau: source venv/bin/activate

# Run app
streamlit run app.py
```

Atau gunakan script:
```bash
# Windows
run_app.bat

# Linux/Mac
./run_app.sh
```

---

## 🔍 Troubleshooting

### Problem: PyTorch tidak terdeteksi GPU

**Solution:**
```bash
# Check CUDA version di system
nvidia-smi

# Install PyTorch yang match dengan CUDA version
# Lihat: https://pytorch.org/get-started/locally/
```

### Problem: `pipenv install` error dengan PyTorch

**Solution:**
Ini normal! PyTorch dengan CUDA tidak bisa diinstall via Pipfile.
1. Run `pipenv install` (akan skip PyTorch)
2. Run `install_pytorch.bat` atau `install_pytorch.sh`

### Problem: Module not found errors

**Solution:**
```bash
# Reinstall dependencies
pipenv install --dev

# Atau untuk venv:
pip install -r requirements.txt
```

### Problem: Out of memory saat training

**Solution:**
1. Reduce batch size di training notebook
2. Enable gradient checkpointing
3. Use CPU instead of GPU (slower)

---

## 📊 Installed Packages Summary

### Core ML/NLP:
- ✅ `transformers` - Hugging Face Transformers
- ✅ `torch` - PyTorch
- ✅ `datasets` - Hugging Face Datasets
- ✅ `evaluate` - Evaluation metrics
- ✅ `rouge-score` - ROUGE metrics
- ✅ `accelerate` - Training acceleration

### Data Processing:
- ✅ `pandas` - Data manipulation
- ✅ `numpy` - Numerical computing
- ✅ `beautifulsoup4` - HTML parsing
- ✅ `sastrawi` - Indonesian stemming

### Visualization:
- ✅ `matplotlib` - Plotting
- ✅ `seaborn` - Statistical visualization
- ✅ `wordcloud` - Word cloud generation

### Development:
- ✅ `jupyter` - Jupyter Notebook
- ✅ `jupyterlab` - JupyterLab
- ✅ `ipykernel` - IPython kernel

### Deployment:
- ✅ `streamlit` - Web app framework

---

## 📝 Environment Files

Project ini menggunakan beberapa file untuk dependency management:

1. **`Pipfile`** - Pipenv dependencies (development)
2. **`requirements.txt`** - pip dependencies (deployment)
3. **`Pipfile.lock`** - Locked versions (pipenv)

**Note**: PyTorch **tidak** included di Pipfile karena masalah compatibility dengan pipenv. Install manual setelah `pipenv install`.

---

## 🆘 Get Help

Jika mengalami masalah:

1. Baca troubleshooting guide di atas
2. Check [PYTORCH_INSTALL.md](PYTORCH_INSTALL.md) untuk detail PyTorch
3. Check [DEPLOYMENT.md](DEPLOYMENT.md) untuk deployment issues
4. Open issue di GitHub repository

---

## ✅ Installation Checklist

Sebelum mulai development/deployment:

- [ ] Python 3.13 installed
- [ ] Pipenv atau venv created
- [ ] Dependencies installed (`pipenv install` atau `pip install -r requirements.txt`)
- [ ] PyTorch dengan GPU installed (via script atau manual)
- [ ] PyTorch CUDA working (`torch.cuda.is_available()` returns `True`)
- [ ] Jupyter notebooks bisa dibuka
- [ ] Streamlit app bisa dijalankan

---

**Last Updated**: November 3, 2025
