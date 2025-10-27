# Liputan6 Dataset Analysis - Text Summarization

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Analisis dataset Liputan6 untuk text summarization menggunakan Python dan Jupyter Notebook.

## 📖 Overview

Project ini melakukan **Exploratory Data Analysis (EDA)** pada dataset Liputan6 untuk memahami karakteristik teks berita Indonesia dan ringkasannya. Analisis mencakup distribusi panjang teks, frekuensi kata, stopwords, dan visualisasi data.

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

- **pandas** - Data manipulation dan analysis
- **numpy** - Numerical computing
- **matplotlib** - Plotting dan visualisasi
- **seaborn** - Statistical data visualization
- **wordcloud** - Word cloud generation
- **sastrawi** - Indonesian language stemming dan stopwords
- **jupyter** - Jupyter notebook
- **ipykernel** - IPython kernel untuk Jupyter

## 📂 File Structure

```
sumarizer-ai/
├── liputan6_data/          # Dataset JSON files
│   └── canonical/
│       ├── train/          # Training data (193,883 files)
│       ├── test/           # Test data
│       └── validation/     # Validation data
├── liputan6_train.csv      # Converted CSV dataset
├── csv_converter.py        # JSON to CSV converter script
├── Liputan6_EDA_Summarization_Colab_v4_2.ipynb  # Main analysis notebook
├── Pipfile                 # Pipenv dependencies
├── Pipfile.lock           # Locked dependencies versions
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

## 📝 Analysis Steps

Notebook ini melakukan analisis sebagai berikut:

1. **Setup & Load Data** - Import libraries dan load CSV
2. **Data Profiling** - Overview kolom dan statistik dasar
3. **Missing Values** - Analisis nilai yang hilang
4. **Text Length Distribution** - Distribusi panjang artikel dan ringkasan
5. **Sentence Count** - Jumlah kalimat per artikel
6. **Article Examples** - Contoh artikel terpendek dan terpanjang
7. **Word Frequency** - Kata-kata yang paling sering muncul
8. **Stopwords Analysis** - Analisis stopwords Bahasa Indonesia

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
