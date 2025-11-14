@echo off
REM Install PyTorch with GPU support after pipenv install
REM This script installs PyTorch with CUDA 11.8 support

echo =========================================
echo   PyTorch GPU Installation Helper
echo =========================================
echo.

REM Check if pipenv is installed
where pipenv >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pipenv not found!
    echo Please install pipenv first: pip install pipenv
    pause
    exit /b 1
)

echo Step 1: Activating pipenv environment...
echo.

REM Create a temporary script to run inside pipenv shell
echo import torch > temp_check.py
echo try: >> temp_check.py
echo     print(f"PyTorch already installed: {torch.__version__}") >> temp_check.py
echo     print(f"CUDA Available: {torch.cuda.is_available()}") >> temp_check.py
echo except: >> temp_check.py
echo     print("PyTorch not installed") >> temp_check.py

pipenv run python temp_check.py
del temp_check.py

echo.
echo =========================================
echo.
echo Select PyTorch installation option:
echo   1. CUDA 11.8 (Most compatible)
echo   2. CUDA 12.1 (Latest)
echo   3. CPU only (No GPU)
echo   4. Skip (already installed)
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Installing PyTorch with CUDA 11.8...
    pipenv run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    goto verify
)

if "%choice%"=="2" (
    echo.
    echo Installing PyTorch with CUDA 12.1...
    pipenv run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    goto verify
)

if "%choice%"=="3" (
    echo.
    echo Installing PyTorch CPU version...
    pipenv run pip install torch torchvision torchaudio
    goto verify
)

if "%choice%"=="4" (
    echo.
    echo Skipping PyTorch installation...
    goto end
)

echo Invalid choice!
pause
exit /b 1

:verify
echo.
echo =========================================
echo   Verifying Installation
echo =========================================
echo.

pipenv run python -c "import torch; print(f'PyTorch Version: {torch.__version__}'); print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'CUDA Version: {torch.version.cuda if torch.cuda.is_available() else \"N/A\"}'); print(f'Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"CPU\"}')"

echo.
echo =========================================

:end
echo.
echo Installation complete!
echo.
echo To use the application:
echo   1. Run: pipenv shell
echo   2. Run: streamlit run app.py
echo.
pause
