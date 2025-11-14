@echo off
REM Liputan6 Text Summarizer - Run Script (Windows)
REM This script sets up and runs the Streamlit application

echo =========================================
echo   Liputan6 Text Summarizer - Streamlit
echo =========================================
echo.

REM Check if model exists
if not exist "output\bert2gpt_finetuned\final_model" (
    echo ERROR: Model not found!
    echo.
    echo Please run the training notebook first:
    echo   1. Open Liputan6_BERT2GPT_Training.ipynb
    echo   2. Run all cells to train and save the model
    echo   3. Model will be saved to: output\bert2gpt_finetuned\final_model\
    echo.
    pause
    exit /b 1
)

echo Model found: output\bert2gpt_finetuned\final_model\
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Install/Update dependencies
echo Installing dependencies...
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo Dependencies installed
echo.

REM Run Streamlit app
echo Starting Streamlit application...
echo.
echo =========================================
echo   Application will open in your browser
echo   Local URL: http://localhost:8501
echo   Press Ctrl+C to stop the server
echo =========================================
echo.

streamlit run app.py
