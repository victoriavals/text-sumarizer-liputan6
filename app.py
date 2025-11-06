"""
Liputan6 Text Summarizer - Streamlit App
BERT2GPT Indonesian Summarization Model
"""

import streamlit as st
import torch
from transformers import BertTokenizer, EncoderDecoderModel
from pathlib import Path
import json
import time

# Page config
st.set_page_config(
    page_title="Liputan6 Text Summarizer",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .article-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .summary-box {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .stats-box {
        background-color: #fff;
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the fine-tuned BERT2GPT model"""
    try:
        # Model path
        model_dir = Path("./output/bert2gpt_finetuned/final_model")
        
        if not model_dir.exists():
            st.error(f"❌ Model directory not found: {model_dir}")
            st.info("💡 Please run the training notebook first to generate the model.")
            return None, None, None
        
        # Load tokenizer
        with st.spinner("Loading tokenizer..."):
            tokenizer = BertTokenizer.from_pretrained(str(model_dir))
            tokenizer.bos_token = tokenizer.cls_token
            tokenizer.eos_token = tokenizer.sep_token
        
        # Load model
        with st.spinner("Loading model..."):
            model = EncoderDecoderModel.from_pretrained(str(model_dir))
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model.to(device)
            model.eval()
        
        # Load training info
        info_path = model_dir / "training_info.json"
        training_info = None
        if info_path.exists():
            with open(info_path, 'r') as f:
                training_info = json.load(f)
        
        return tokenizer, model, training_info
    
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        return None, None, None

def generate_summary(article_text, tokenizer, model, num_beams=10, min_length=20, max_length=80):
    """Generate summary for a given article"""
    device = next(model.parameters()).device
    
    # Tokenize input
    input_ids = tokenizer.encode(
        article_text, 
        return_tensors='pt', 
        max_length=512, 
        truncation=True
    )
    input_ids = input_ids.to(device)
    
    # Generate summary
    with torch.no_grad():
        summary_ids = model.generate(
            input_ids,
            min_length=min_length,
            max_length=max_length,
            num_beams=num_beams,
            repetition_penalty=2.5,
            length_penalty=1.0,
            early_stopping=True,
            no_repeat_ngram_size=2,
            use_cache=True,
            do_sample=True,
            temperature=0.8,
            top_k=50,
            top_p=0.95
        )
    
    # Decode summary
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary_text

def main():
    # Header
    st.markdown('<h1 class="main-header">📰 Liputan6 Text Summarizer</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Ringkas artikel berita Indonesia menggunakan AI (BERT2GPT)</p>', unsafe_allow_html=True)
    
    # Load model
    tokenizer, model, training_info = load_model()
    
    if tokenizer is None or model is None:
        st.stop()
    
    # Success message
    device = next(model.parameters()).device
    st.success(f"✅ Model loaded successfully! Running on: **{device}**")
    
    # Sidebar - Model Info
    with st.sidebar:
        st.header("ℹ️ Model Information")
        
        if training_info:
            st.write("**Model:**", training_info.get('model_checkpoint', 'N/A'))
            st.write("**Training Samples:**", f"{training_info.get('train_samples', 0):,}")
            st.write("**Epochs:**", training_info.get('num_epochs', 'N/A'))
            st.write("**Learning Rate:**", training_info.get('learning_rate', 'N/A'))
            
            # Test metrics
            test_metrics = training_info.get('test_metrics', {})
            if test_metrics:
                st.subheader("📊 Test Metrics")
                for key, value in test_metrics.items():
                    if 'rouge' in key.lower():
                        st.metric(key.upper(), f"{value:.2f}")
        
        st.divider()
        
        # Generation parameters
        st.header("⚙️ Generation Settings")
        num_beams = st.slider("Beam Search Width", 1, 15, 10, help="Higher = better quality, slower")
        min_length = st.slider("Min Summary Length", 10, 50, 20, help="Minimum words in summary")
        max_length = st.slider("Max Summary Length", 30, 150, 80, help="Maximum words in summary")
        
        st.divider()
        
        # About
        st.header("📚 About")
        st.write("""
        Model ini menggunakan arsitektur **BERT-to-GPT2** untuk meringkas artikel berita berbahasa Indonesia.
        
        **Dataset:** Liputan6 News Articles
        
        **Model:** cahya/bert2gpt-indonesian-summarization
        """)
    
    # Main content - Tabs
    tab1, tab2 = st.tabs(["✍️ Input Manual", "📋 Contoh Artikel"])
    
    with tab1:
        st.subheader("Masukkan Artikel Anda")
        
        article_input = st.text_area(
            "Artikel:",
            height=300,
            placeholder="Paste artikel berita di sini...\n\nContoh:\nJakarta - Presiden Joko Widodo mengumumkan..."
        )
        
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            summarize_btn = st.button("🚀 Generate Summary", type="primary", use_container_width=True)
        with col2:
            clear_btn = st.button("🗑️ Clear", use_container_width=True)
        
        if clear_btn:
            st.rerun()
        
        if summarize_btn:
            if not article_input.strip():
                st.warning("⚠️ Please enter an article first!")
            else:
                process_article(article_input, tokenizer, model, num_beams, min_length, max_length)
    
    with tab2:
        st.subheader("Pilih Contoh Artikel")
        
        examples = {
            "Politik - Kebijakan Digital": """
            Jakarta - Presiden Joko Widodo (Jokowi) mengumumkan kebijakan baru terkait pengembangan 
            infrastruktur digital di Indonesia. Pemerintah akan mengalokasikan dana triliunan rupiah 
            untuk mempercepat pembangunan jaringan internet di daerah terpencil. Langkah ini diharapkan 
            dapat mengurangi kesenjangan digital antara kota besar dan daerah pedalaman. Menteri 
            Komunikasi dan Informatika menyatakan bahwa program ini akan dimulai tahun depan dengan 
            target mencakup 10.000 desa dalam tahap pertama.
            """,
            "Ekonomi - Kenaikan Harga": """
            Jakarta - Harga bahan bakar minyak (BBM) diprediksi akan naik pada bulan depan seiring 
            dengan kenaikan harga minyak dunia. Kementerian Energi dan Sumber Daya Mineral (ESDM) 
            menyatakan bahwa pemerintah sedang mengkaji berbagai opsi untuk meredam dampak kenaikan 
            harga BBM terhadap masyarakat. Salah satu opsi yang dipertimbangkan adalah pemberian 
            subsidi tambahan untuk kelompok masyarakat berpenghasilan rendah. Analis ekonomi 
            memperkirakan kenaikan harga BBM dapat memicu inflasi hingga 5 persen.
            """,
            "Pendidikan - Kurikulum Baru": """
            Jakarta - Kementerian Pendidikan dan Kebudayaan meluncurkan kurikulum baru yang akan 
            diterapkan di seluruh sekolah mulai tahun ajaran berikutnya. Kurikulum ini menekankan 
            pada pengembangan keterampilan abad ke-21 seperti critical thinking, kreativitas, dan 
            kolaborasi. Menteri Pendidikan menyatakan bahwa kurikulum baru ini dirancang untuk 
            mempersiapkan siswa menghadapi tantangan masa depan. Program pelatihan guru akan 
            dilaksanakan secara bertahap di seluruh provinsi untuk memastikan implementasi yang efektif.
            """,
            "Kesehatan - Vaksinasi": """
            Jakarta - Program vaksinasi COVID-19 tahap ketiga akan dimulai minggu depan dengan target 
            50 juta penduduk. Pemerintah telah menyiapkan 100 ribu tenaga kesehatan dan 10 ribu 
            fasilitas vaksinasi di seluruh Indonesia. Kementerian Kesehatan mengimbau masyarakat 
            untuk segera mendaftar melalui aplikasi resmi. Vaksin yang akan digunakan adalah jenis 
            mRNA dengan efektivitas mencapai 95 persen. Prioritas vaksinasi diberikan kepada lansia 
            dan penderita penyakit komorbid.
            """
        }
        
        selected_example = st.selectbox("Pilih contoh:", list(examples.keys()))
        
        example_article = examples[selected_example]
        st.markdown('<div class="article-box">', unsafe_allow_html=True)
        st.write(example_article.strip())
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🚀 Generate Summary untuk Contoh Ini", type="primary"):
            process_article(example_article, tokenizer, model, num_beams, min_length, max_length)
    
    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>Built with ❤️ using Streamlit & Hugging Face Transformers</p>
        <p>Model: <a href='https://huggingface.co/cahya/bert2gpt-indonesian-summarization' target='_blank'>cahya/bert2gpt-indonesian-summarization</a></p>
    </div>
    """, unsafe_allow_html=True)

def process_article(article_text, tokenizer, model, num_beams, min_length, max_length):
    """Process and display article summary"""
    # Show original article
    st.markdown("---")
    st.subheader("📄 Artikel Asli")
    st.markdown('<div class="article-box">', unsafe_allow_html=True)
    st.write(article_text.strip())
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate summary with progress
    with st.spinner("🤖 Generating summary..."):
        start_time = time.time()
        summary = generate_summary(
            article_text.strip(),
            tokenizer,
            model,
            num_beams=num_beams,
            min_length=min_length,
            max_length=max_length
        )
        generation_time = time.time() - start_time
    
    # Show summary
    st.subheader("📝 Ringkasan")
    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
    st.write(summary)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistics
    st.subheader("📊 Statistics")
    
    article_words = len(article_text.split())
    summary_words = len(summary.split())
    compression_ratio = (summary_words / article_words * 100) if article_words > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="stats-box">', unsafe_allow_html=True)
        st.metric("Article Length", f"{article_words} words")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="stats-box">', unsafe_allow_html=True)
        st.metric("Summary Length", f"{summary_words} words")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="stats-box">', unsafe_allow_html=True)
        st.metric("Compression", f"{compression_ratio:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="stats-box">', unsafe_allow_html=True)
        st.metric("Generation Time", f"{generation_time:.2f}s")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Download button
    st.download_button(
        label="💾 Download Summary",
        data=f"ARTIKEL:\n{article_text}\n\n{'='*80}\n\nRINGKASAN:\n{summary}\n\n{'='*80}\n\nSTATISTICS:\n- Article: {article_words} words\n- Summary: {summary_words} words\n- Compression: {compression_ratio:.1f}%\n- Time: {generation_time:.2f}s",
        file_name="summary.txt",
        mime="text/plain"
    )

if __name__ == "__main__":
    main()
