"""
Script untuk membuat sample 5% dari setiap dataset (train, test, validation)
Untuk mempercepat proses pelatihan dan eksperimen
"""

import pandas as pd
import os

# Paths untuk file asli
TRAIN_PATH = "liputan6_train.csv"
TEST_PATH = "liputan6_test.csv"
VAL_PATH = "liputan6_validation.csv"

# Paths untuk file sample (5%)
TRAIN_SAMPLE_PATH = "liputan6_train_sample5.csv"
TEST_SAMPLE_PATH = "liputan6_test_sample5.csv"
VAL_SAMPLE_PATH = "liputan6_validation_sample5.csv"

# Persentase sample
SAMPLE_FRACTION = 0.05  # 5%

print("=" * 60)
print("Creating 5% Sample Datasets")
print("=" * 60)

def create_sample(input_path, output_path, fraction=0.05, random_state=42):
    """
    Membuat sample random dari dataset
    
    Args:
        input_path: Path ke file CSV input
        output_path: Path ke file CSV output
        fraction: Persentase data yang diambil (default 0.05 = 5%)
        random_state: Seed untuk reproducibility
    """
    try:
        # Load dataset
        print(f"\n📂 Loading {input_path}...")
        df = pd.read_csv(input_path, low_memory=False)
        print(f"   Original size: {len(df)} rows")
        
        # Ambil sample random
        df_sample = df.sample(frac=fraction, random_state=random_state)
        
        # Reset index
        df_sample = df_sample.reset_index(drop=True)
        
        # Save to CSV
        df_sample.to_csv(output_path, index=False)
        print(f"   Sample size: {len(df_sample)} rows ({fraction*100:.1f}%)")
        print(f"   ✓ Saved to: {output_path}")
        
        return len(df), len(df_sample)
        
    except FileNotFoundError:
        print(f"   ❌ Error: File not found - {input_path}")
        return 0, 0
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return 0, 0

# Process all datasets
print(f"\n🎯 Creating {SAMPLE_FRACTION*100:.0f}% samples from all datasets...\n")

# Train dataset
train_orig, train_sample = create_sample(TRAIN_PATH, TRAIN_SAMPLE_PATH, SAMPLE_FRACTION)

# Test dataset
test_orig, test_sample = create_sample(TEST_PATH, TEST_SAMPLE_PATH, SAMPLE_FRACTION)

# Validation dataset
val_orig, val_sample = create_sample(VAL_PATH, VAL_SAMPLE_PATH, SAMPLE_FRACTION)

# Summary
print("\n" + "=" * 60)
print("✅ Sample Creation Complete!")
print("=" * 60)
print(f"\n📊 Summary:")
print(f"  Train:      {train_orig:,} → {train_sample:,} rows")
print(f"  Test:       {test_orig:,} → {test_sample:,} rows")
print(f"  Validation: {val_orig:,} → {val_sample:,} rows")
print(f"  Total:      {train_orig + test_orig + val_orig:,} → {train_sample + test_sample + val_sample:,} rows")

print(f"\n📁 Sample files created:")
print(f"  • {TRAIN_SAMPLE_PATH}")
print(f"  • {TEST_SAMPLE_PATH}")
print(f"  • {VAL_SAMPLE_PATH}")

print(f"\n💡 Tip: Update notebook to use these sample files:")
print(f"   TRAIN_PATH = '{TRAIN_SAMPLE_PATH}'")
print(f"   TEST_PATH = '{TEST_SAMPLE_PATH}'")
print(f"   VAL_PATH = '{VAL_SAMPLE_PATH}'")
