# 🚀 Deployment Guide - Liputan6 Text Summarizer

Panduan lengkap untuk deployment aplikasi Streamlit Liputan6 Text Summarizer.

## 📋 Prerequisites

1. **Model yang sudah di-training**
   - Pastikan Anda sudah menjalankan `Liputan6_BERT2GPT_Training.ipynb`
   - Model harus tersimpan di: `./output/bert2gpt_finetuned/final_model/`

2. **Python 3.8+** (Recommended: Python 3.13)

## 🛠️ Setup Lokal

### Opsi 1: Menggunakan Pipenv (Recommended untuk Development)

```bash
# Install pipenv jika belum ada
pip install pipenv

# Install dependencies
pipenv install

# Tambahkan streamlit
pipenv install streamlit==1.39.0

# Activate environment
pipenv shell

# Run aplikasi
streamlit run app.py
```

### Opsi 2: Menggunakan pip + venv (Recommended untuk Deployment)

```bash
# Buat virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run aplikasi
streamlit run app.py
```

### Opsi 3: Direct Install (Tidak Recommended)

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Akses Aplikasi

Setelah menjalankan `streamlit run app.py`, aplikasi akan tersedia di:

- **Local URL**: http://localhost:8501
- **Network URL**: http://192.168.x.x:8501 (untuk akses dari device lain di network yang sama)

## 📦 Deployment ke Cloud

### Streamlit Cloud (Gratis, Paling Mudah)

1. **Push code ke GitHub**
   ```bash
   git add .
   git commit -m "Add Streamlit deployment"
   git push origin master
   ```

2. **Deploy di Streamlit Cloud**
   - Kunjungi: https://streamlit.io/cloud
   - Sign in dengan GitHub
   - Click "New app"
   - Pilih repository: `text-sumarizer-liputan6`
   - Main file path: `app.py`
   - Click "Deploy"

3. **Catatan Penting untuk Streamlit Cloud**
   - Model size harus < 1GB (karena limit Streamlit Cloud)
   - Jika model terlalu besar, pertimbangkan:
     - Gunakan model quantization
     - Deploy ke Hugging Face Spaces
     - Gunakan cloud storage (Google Drive, S3) untuk model

### Hugging Face Spaces

1. **Buat file `requirements.txt` minimal**
   ```txt
   streamlit==1.39.0
   torch==2.5.1
   transformers==4.57.1
   ```

2. **Upload ke Hugging Face Spaces**
   ```bash
   # Clone space
   git clone https://huggingface.co/spaces/YOUR_USERNAME/liputan6-summarizer
   cd liputan6-summarizer
   
   # Copy files
   cp /path/to/app.py .
   cp /path/to/requirements.txt .
   cp -r /path/to/output/bert2gpt_finetuned/final_model ./model
   
   # Commit and push
   git add .
   git commit -m "Initial deployment"
   git push
   ```

### Heroku (Bayar)

1. **Install Heroku CLI**
   ```bash
   # Download dari: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Buat Procfile**
   ```bash
   echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create liputan6-summarizer
   git push heroku master
   ```

### Docker (Untuk semua platform)

1. **Buat Dockerfile**
   ```dockerfile
   FROM python:3.13-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY app.py .
   COPY output/bert2gpt_finetuned/final_model ./output/bert2gpt_finetuned/final_model
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build dan Run**
   ```bash
   # Build image
   docker build -t liputan6-summarizer .
   
   # Run container
   docker run -p 8501:8501 liputan6-summarizer
   ```

## ⚙️ Konfigurasi

### Streamlit Config

Buat file `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
enableCORS = false
enableXsrfProtection = true
```

### Environment Variables

Buat file `.env` untuk konfigurasi:

```env
MODEL_PATH=./output/bert2gpt_finetuned/final_model
MAX_INPUT_LENGTH=512
DEFAULT_NUM_BEAMS=10
DEFAULT_MAX_LENGTH=80
```

## 🔧 Optimasi untuk Production

### 1. Model Optimization

**Quantization** (mengurangi ukuran model):
```python
# Tambahkan di load_model()
model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)
```

### 2. Caching

App sudah menggunakan `@st.cache_resource` untuk cache model loading.

### 3. Memory Management

Untuk server dengan memory terbatas, tambahkan:
```python
# Di app.py, setelah generate
torch.cuda.empty_cache()  # Jika pakai GPU
```

## 📊 Monitoring

### Streamlit Cloud
- Built-in analytics di dashboard
- Log viewing di web interface

### Self-hosted
Install monitoring:
```bash
pip install streamlit-analytics
```

Tambahkan di `app.py`:
```python
import streamlit_analytics

with streamlit_analytics.track():
    main()
```

## 🐛 Troubleshooting

### Error: Model not found
```
✅ Solution: Pastikan path model benar
- Check: ./output/bert2gpt_finetuned/final_model/ exists
- Run training notebook dulu jika belum
```

### Error: Out of memory
```
✅ Solution:
1. Kurangi max_length di sidebar
2. Gunakan CPU instead of GPU untuk inference
3. Enable model quantization
```

### Error: Port already in use
```
✅ Solution: Ganti port
streamlit run app.py --server.port=8502
```

## 📝 Checklist Sebelum Deploy

- [ ] Model sudah di-training dan tersimpan di `output/bert2gpt_finetuned/final_model/`
- [ ] `requirements.txt` sudah di-update
- [ ] Test aplikasi di lokal dengan `streamlit run app.py`
- [ ] Model size < 1GB (untuk Streamlit Cloud) atau gunakan external storage
- [ ] `.gitignore` sudah exclude file besar dan sensitive data
- [ ] README.md sudah di-update
- [ ] Repository sudah di-push ke GitHub

## 🔒 Security Notes

1. **Jangan commit file besar** (.bin, .pkl > 100MB) ke Git
2. **Gunakan Git LFS** untuk model files
3. **Hide sensitive info** di `.env` dan `.gitignore`
4. **Enable authentication** untuk production

## 📚 Resources

- Streamlit Docs: https://docs.streamlit.io
- Streamlit Cloud: https://streamlit.io/cloud
- Hugging Face Spaces: https://huggingface.co/spaces
- Docker Hub: https://hub.docker.com

## 💡 Tips

1. **Test lokal dulu** sebelum deploy
2. **Start simple** - deploy minimal version dulu
3. **Monitor usage** - cek logs dan analytics
4. **Update regular** - keep dependencies up to date
5. **Backup model** - simpan di cloud storage

---

**Happy Deploying! 🚀**
