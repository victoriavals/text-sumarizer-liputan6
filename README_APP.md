# 📰 Liputan6 Text Summarizer - Streamlit App

Web application untuk meringkas artikel berita Indonesia menggunakan model BERT2GPT yang telah di-fine-tune.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red)
![Transformers](https://img.shields.io/badge/Transformers-4.57.1-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 📝 **Text Summarization** - Ringkas artikel berita Indonesia secara otomatis
- 🎯 **BERT2GPT Model** - Menggunakan model state-of-the-art untuk bahasa Indonesia
- 🎨 **User-friendly Interface** - Antarmuka yang mudah digunakan
- ⚙️ **Customizable Parameters** - Atur panjang ringkasan dan kualitas generasi
- 📊 **Statistics** - Lihat statistik kompresi dan performa
- 💾 **Download Results** - Download ringkasan dalam format teks
- 🚀 **Fast Inference** - Generasi ringkasan dalam hitungan detik

## 🖼️ Screenshots

### Home Page
Interface utama dengan input artikel manual atau pilihan contoh artikel.

### Generation Settings
Sidebar dengan pengaturan parameter generasi:
- Beam Search Width
- Minimum Summary Length
- Maximum Summary Length

### Results Display
Tampilan artikel asli, ringkasan, dan statistik kompresi.

## 🚀 Quick Start

### Prasyarat

1. **Model yang sudah di-training**
   ```bash
   # Pastikan model ada di path ini:
   ./output/bert2gpt_finetuned/final_model/
   ```

2. **Python 3.8+** (Recommended: 3.13)

### Installation & Run

#### Windows (PowerShell/CMD):
```bash
# Double click atau run:
run_app.bat
```

#### Linux/Mac (Bash):
```bash
# Make executable dan run:
chmod +x run_app.sh
./run_app.sh
```

#### Manual Setup:
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate (Windows)
venv\Scripts\activate
# Or (Linux/Mac)
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run app
streamlit run app.py
```

### Menggunakan Pipenv:
```bash
# Install pipenv
pip install pipenv

# Install dependencies
pipenv install

# Run app
pipenv run streamlit run app.py
```

## 📖 Usage

1. **Start the application**
   - Aplikasi akan terbuka otomatis di browser
   - URL: http://localhost:8501

2. **Input Article**
   - **Tab "Input Manual"**: Paste artikel Anda sendiri
   - **Tab "Contoh Artikel"**: Pilih dari contoh yang disediakan

3. **Adjust Settings** (Optional)
   - Sidebar → Generation Settings
   - Atur parameter sesuai kebutuhan

4. **Generate Summary**
   - Click tombol "🚀 Generate Summary"
   - Tunggu beberapa detik untuk hasil

5. **View Results**
   - Lihat ringkasan yang dihasilkan
   - Check statistik kompresi
   - Download hasil jika diperlukan

## ⚙️ Configuration

### Generation Parameters

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| **Beam Search Width** | 10 | 1-15 | Higher = better quality, slower |
| **Min Summary Length** | 20 | 10-50 | Minimum words in summary |
| **Max Summary Length** | 80 | 30-150 | Maximum words in summary |

### Advanced Config

Edit `.streamlit/config.toml` untuk kustomisasi tema dan server settings.

## 🏗️ Architecture

```
app.py
├── load_model()          # Load BERT2GPT model (cached)
├── generate_summary()    # Generate summary from article
├── process_article()     # Process and display results
└── main()               # Main Streamlit app
```

### Model Pipeline

```
Input Article
    ↓
Tokenization (BertTokenizer)
    ↓
BERT2GPT Model
    ↓
Beam Search Decoding
    ↓
Generated Summary
```

## 📊 Performance

### Inference Time
- **CPU**: ~5-15 seconds per article
- **GPU**: ~1-3 seconds per article

### Model Size
- **Model**: ~400MB (BERT encoder + GPT2 decoder)
- **Memory Usage**: ~2GB RAM (inference)

### Quality Metrics
Check model info in sidebar untuk ROUGE scores:
- ROUGE-1: Unigram overlap
- ROUGE-2: Bigram overlap
- ROUGE-L: Longest common subsequence

## 🐛 Troubleshooting

### Model Not Found
```
❌ Error: Model directory not found
✅ Solution: Run Liputan6_BERT2GPT_Training.ipynb first
```

### Out of Memory
```
❌ Error: CUDA out of memory
✅ Solution: 
- Kurangi max_length di settings
- Gunakan CPU mode
- Close other applications
```

### Port Already in Use
```
❌ Error: Address already in use
✅ Solution: 
streamlit run app.py --server.port=8502
```

### Slow Generation
```
❌ Issue: Summary generation is slow
✅ Solution:
- Reduce beam search width
- Use GPU if available
- Reduce max summary length
```

## 🚀 Deployment

Lihat [DEPLOYMENT.md](DEPLOYMENT.md) untuk panduan lengkap deployment ke:
- Streamlit Cloud (Gratis)
- Hugging Face Spaces
- Heroku
- Docker
- AWS/GCP/Azure

### Quick Deploy to Streamlit Cloud

1. Push ke GitHub
2. Kunjungi https://streamlit.io/cloud
3. Connect repository
4. Deploy!

## 🔧 Development

### Project Structure
```
liputan6-text-sumarizer/
├── app.py                      # Main Streamlit app
├── requirements.txt            # Dependencies
├── Pipfile                     # Pipenv config
├── DEPLOYMENT.md              # Deployment guide
├── run_app.bat                # Windows run script
├── run_app.sh                 # Linux/Mac run script
├── Dockerfile                 # Docker config
├── Procfile                   # Heroku config
├── .streamlit/
│   └── config.toml            # Streamlit config
└── output/
    └── bert2gpt_finetuned/
        └── final_model/       # Trained model
            ├── config.json
            ├── pytorch_model.bin
            ├── tokenizer_config.json
            └── vocab.txt
```

### Adding New Features

1. **Custom Preprocessing**
   ```python
   # Modify in app.py
   def preprocess_text(text):
       # Your custom preprocessing
       return cleaned_text
   ```

2. **Additional Statistics**
   ```python
   # Add to process_article()
   st.metric("New Metric", value)
   ```

3. **Theme Customization**
   ```toml
   # Edit .streamlit/config.toml
   [theme]
   primaryColor = "#your_color"
   ```

## 📚 Documentation

- **Streamlit**: https://docs.streamlit.io
- **Transformers**: https://huggingface.co/docs/transformers
- **Model**: https://huggingface.co/cahya/bert2gpt-indonesian-summarization

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## 👥 Authors

- **Your Name** - Initial work

## 🙏 Acknowledgments

- Model: [cahya/bert2gpt-indonesian-summarization](https://huggingface.co/cahya/bert2gpt-indonesian-summarization)
- Dataset: Liputan6 Indonesian News
- Framework: Hugging Face Transformers
- UI: Streamlit

## 📞 Support

Jika ada pertanyaan atau masalah:
1. Check [Troubleshooting](#-troubleshooting)
2. Read [DEPLOYMENT.md](DEPLOYMENT.md)
3. Open an issue on GitHub

---

**Made with ❤️ using Streamlit & Hugging Face Transformers**
