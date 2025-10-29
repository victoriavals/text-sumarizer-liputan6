# Liputan6 Dataset Analysis - Text Summarization

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Analisis dataset Liputan6 untuk text summarization menggunakan Python dan Jupyter Notebook.

## 📖 Overview

Project ini melakukan **Exploratory Data Analysis (EDA)** dan **Preprocessing** lengkap pada dataset Liputan6 untuk text summarization. Project ini menyediakan pipeline preprocessing yang siap digunakan untuk training model **Seq2Seq** dan **BERT Transformer**.

### Features:
- ✅ Comprehensive EDA dengan visualisasi
- ✅ Data cleaning dan normalization
- ✅ Tokenisasi (word-level & subword)
- ✅ Stopword removal & stemming (Sastrawi)
- ✅ Outlier detection & removal
- ✅ Vocabulary building & encoding
- ✅ Train/val/test split (70/15/15)
- ✅ Ready-to-use preprocessed data untuk training

## 📋 Prerequisites

- Python 3.13 atau lebih baru
- pipenv

## 🚀 Quick Start

### 1. Install Dependencies

```powershell
# Install semua dependencies dari Pipfile
python -m pipenv install
```

### 2. Activate Virtual Environment

```powershell
# Masuk ke virtual environment
python -m pipenv shell
```

### 3. Run Jupyter Notebook

Setelah masuk ke virtual environment, jalankan Jupyter:

```powershell
jupyter notebook
```

Atau langsung buka file notebook:

```powershell
jupyter notebook Liputan6_EDA_Summarization_Colab_v4_2.ipynb
```

### 4. Run di VS Code

Jika menggunakan VS Code:
1. Buka file `Liputan6_EDA_Summarization_Colab_v4_2.ipynb`
2. Pilih kernel yang sesuai (Python 3.13 dari pipenv)
3. Run cells secara berurutan

## 📦 Installed Libraries

### Core Data Processing:
- **pandas** - Data manipulation dan analysis
- **numpy** - Numerical computing
- **beautifulsoup4** - HTML parsing dan cleaning

### Visualization:
- **matplotlib** - Plotting dan visualisasi
- **seaborn** - Statistical data visualization
- **wordcloud** - Word cloud generation

### Indonesian NLP:
- **sastrawi** - Indonesian language stemming dan stopwords

### Machine Learning:
- **scikit-learn** - Train/test split, preprocessing utilities
- **torch** - PyTorch for deep learning
- **transformers** - Hugging Face transformers (BERT, IndoBERT)

### Development:
- **jupyter** - Jupyter notebook
- **ipykernel** - IPython kernel untuk Jupyter

## 📂 File Structure

```
liputan6-text-summarizer/
├── liputan6_data/          # Dataset JSON files
│   └── canonical/
│       ├── train/          # Training data (193,883 files)
│       ├── test/           # Test data
│       └── validation/     # Validation data
├── output/
│   └── preprocessed/       # Preprocessed data (generated after running notebook)
│       ├── train.csv
│       ├── val.csv
│       ├── test.csv
│       ├── vocab_seq2seq.pkl
│       ├── config.json
│       ├── X_train_seq2seq.npy
│       ├── y_train_seq2seq.npy
│       └── bert_data.pkl
├── liputan6_train.csv      # Converted CSV dataset
├── csv_converter.py        # JSON to CSV converter script
├── Liputan6_EDA_Summarization_Colab_v4_2.ipynb  # Main EDA + Preprocessing notebook
├── requirements.txt        # Python dependencies
├── Pipfile                 # Pipenv dependencies
├── Pipfile.lock           # Locked dependencies versions
├── PREPROCESSING_GUIDE.md  # Detailed preprocessing documentation
├── QUICKSTART.md          # Quick start guide
└── README.md              # This file
```

## 📊 Dataset

Dataset berisi artikel berita dari Liputan6 dengan:
- **193,883 artikel** (training data)
- **5 kolom**: id, url, article, summary, extractive_summary

### Kolom Dataset:
- `id`: ID unik artikel
- `url`: URL artikel asli
- `article`: Teks artikel lengkap
- `summary`: Ringkasan artikel
- `extractive_summary`: Index kalimat untuk ringkasan ekstraktif

## 🔧 Useful Commands

### Pipenv Commands

```powershell
# Install package baru
python -m pipenv install <package-name>

# Install dev dependencies
python -m pipenv install --dev <package-name>

# Uninstall package
python -m pipenv uninstall <package-name>

# Update semua packages
python -m pipenv update

# Lihat dependency graph
python -m pipenv graph

# Check security vulnerabilities
python -m pipenv check

# Keluar dari virtual environment
exit
```

### Run Python Scripts

```powershell
# Run script di dalam virtual environment (tanpa masuk shell)
python -m pipenv run python csv_converter.py

# Atau masuk ke shell dulu
python -m pipenv shell
python csv_converter.py
```

## 📝 Notebook Contents

### Part 1: EDA (Langkah 1-9)
1. **Setup & Load Data** - Import libraries dan load CSV
2. **Data Profiling** - Overview kolom dan statistik dasar
3. **Missing Values** - Analisis nilai yang hilang dengan visualisasi
4. **Text Length Distribution** - Distribusi panjang artikel dan ringkasan
5. **Sentence Count** - Jumlah kalimat per artikel
6. **Article Examples** - Contoh artikel terpendek dan terpanjang
7. **Word Frequency** - Kata-kata yang paling sering muncul (dengan WordCloud)
8. **Stopwords Analysis** - Analisis stopwords Bahasa Indonesia

### Part 2: Preprocessing (Langkah 10-20)
10. **Data Cleaning** - HTML removal, normalization, whitespace handling
11. **Remove Duplicates** - Menghapus artikel duplikat
12. **Tokenization** - Word-level tokenization untuk Seq2Seq
13. **Stopword Removal & Stemming** - Sastrawi untuk Seq2Seq (preserved untuk BERT)
14. **Noise & Outlier Removal** - Filter data berkualitas rendah
15. **BERT Tokenization** - Subword tokenization dengan IndoBERT/mBERT
16. **Vocabulary Building** - Build vocabulary dan encoding untuk Seq2Seq
17. **Padding & Sequence Preparation** - Uniform sequence lengths
18. **Train/Val/Test Split** - 70/15/15 split dengan validation
19. **Preprocessing Validation** - Quality checks
20. **Save Preprocessed Data** - Export untuk training

## 🚀 Usage

### Step 1: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 2: Run the Notebook

Open and run `Liputan6_EDA_Summarization_Colab_v4_2.ipynb` in Jupyter or Google Colab.

### Step 3: Use Preprocessed Data

After running the notebook, use the preprocessed data for model training:

**For Seq2Seq models:**
```python
import numpy as np
X_train = np.load('output/preprocessed/X_train_seq2seq.npy')
y_train = np.load('output/preprocessed/y_train_seq2seq.npy')
```

**For BERT models:**
```python
import pickle
with open('output/preprocessed/bert_data.pkl', 'rb') as f:
    data = pickle.load(f)
```

See `QUICKSTART.md` for detailed examples and `PREPROCESSING_GUIDE.md` for complete documentation.

## 🐛 Troubleshooting

### Error: pipenv not recognized

Gunakan `python -m pipenv` sebagai pengganti `pipenv`:

```powershell
python -m pipenv install
python -m pipenv shell
```

### Kernel tidak ditemukan di VS Code

1. Install ipykernel: `python -m pipenv install ipykernel`
2. Reload VS Code
3. Pilih kernel dari Command Palette (Ctrl+Shift+P) → "Select Kernel"

### CSV file tidak ditemukan

Jalankan converter terlebih dahulu:

```powershell
python -m pipenv run python csv_converter.py
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is licensed under the MIT License. Dataset bersumber dari Liputan6.

## 👤 Author

**Naufal Firdaus**

- GitHub: [@NaufalFirdaus](https://github.com/NaufalFirdaus)

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

**Note:** Dataset files (`*.csv`, `*.json`, `liputan6_data/`) tidak di-commit ke repository karena ukurannya yang besar. Silakan download dataset secara terpisah.
