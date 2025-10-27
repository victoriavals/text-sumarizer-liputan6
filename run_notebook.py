# Helper script untuk menjalankan Jupyter Notebook dengan pipenv
# Run this script: python -m pipenv run python run_notebook.py

import subprocess
import sys

def main():
    print("🚀 Starting Jupyter Notebook with pipenv environment...")
    print("=" * 60)
    
    try:
        # Run jupyter notebook
        subprocess.run([
            sys.executable, 
            "-m", 
            "jupyter", 
            "notebook", 
            "Liputan6_EDA_Summarization_Colab_v4_2.ipynb"
        ], check=True)
    except KeyboardInterrupt:
        print("\n\n✅ Jupyter Notebook closed.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running Jupyter: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
