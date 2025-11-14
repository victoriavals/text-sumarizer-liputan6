#!/bin/bash

# Liputan6 Text Summarizer - Run Script
# This script sets up and runs the Streamlit application

echo "========================================="
echo "  Liputan6 Text Summarizer - Streamlit"
echo "========================================="
echo ""

# Check if model exists
if [ ! -d "./output/bert2gpt_finetuned/final_model" ]; then
    echo "❌ ERROR: Model not found!"
    echo ""
    echo "Please run the training notebook first:"
    echo "  1. Open Liputan6_BERT2GPT_Training.ipynb"
    echo "  2. Run all cells to train and save the model"
    echo "  3. Model will be saved to: ./output/bert2gpt_finetuned/final_model/"
    echo ""
    exit 1
fi

echo "✅ Model found: ./output/bert2gpt_finetuned/final_model/"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
    echo "✅ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/Mac
    source venv/bin/activate
fi
echo "✅ Virtual environment activated"
echo ""

# Install/Update dependencies
echo "📦 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Run Streamlit app
echo "🚀 Starting Streamlit application..."
echo ""
echo "========================================="
echo "  Application will open in your browser"
echo "  Local URL: http://localhost:8501"
echo "  Press Ctrl+C to stop the server"
echo "========================================="
echo ""

streamlit run app.py
