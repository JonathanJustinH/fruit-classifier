import streamlit as st
from PIL import Image
from classify import classify_fruit
import pathlib

# Set page configuration
st.set_page_config(
    page_title="FreshFruit AI - Fruit Freshness Classifier",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'uploaded_filename' not in st.session_state:
    st.session_state.uploaded_filename = None
    st.session_state.results = None
    st.session_state.classified = False

# Load and inject global CSS
css_path = pathlib.Path(__file__).parent / "styles.css"
css = css_path.read_text()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Custom HTML layout
st.markdown("""
<div class="main-container">
    <!-- Header -->
    <div class="header">
        <div class="logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2Z" fill="#22C55E" fill-opacity="0.2" stroke="#22C55E" stroke-width="2"/>
                <path d="M12 6.5C12 6.5 10 6.5 9.5 8.5C9 10.5 10.5 11 10.5 11C10.5 11 10 9.5 11 9C12 8.5 12 6.5 12 6.5Z" fill="#22C55E"/>
            </svg>
            <span class="logo-text">FreshFruit AI</span>
        </div>
        <div class="beta-badge">Beta</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Create columns for the main content
col1, col2 = st.columns(2)

# Store state
if 'classified' not in st.session_state:
    st.session_state.classified = False
    
if 'results' not in st.session_state:
    st.session_state.results = None

# Custom upload card
with col1:
    st.markdown("""
    <div class="card">
        <h2 class="card-title">Upload Fruit Image</h2>
        <div style="margin-top: 16px;">
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        label="Upload your fruit image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    # If a new file is uploaded, reset previous results
    if uploaded_file is not None:
        if st.session_state.uploaded_filename != uploaded_file.name:
            st.session_state.uploaded_filename = uploaded_file.name
            st.session_state.results = None
            st.session_state.classified = False

        # Show preview
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

        # Classify button next to preview
        if st.button("Classify Fruit", key="classify_btn"):
            with st.spinner("Analyzing..."):
                st.session_state.results = classify_fruit(image)
                st.session_state.classified = True

# Results card
with col2:
    if not st.session_state.classified:
        st.markdown(
            """
            <div class="card" style="height: 400px;">
              <h2 class="card-title">Classification Results</h2>
              <div class="results-placeholder">
                <p>Upload an image to see results</p>
              </div>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        results = st.session_state.results
        freshness = results["freshness"]  # "fresh" / "mild" / "rotten"
        conf = round(results["confidence"], 2)

        # map each label to an icon and CSS class
        icon_map = {
            "fresh":    ("✓", "fresh-icon"),
            "mild":     ("●", "mild-icon"),
            "rotten":   ("✗", "rotten-icon")
        }
        icon_symbol, icon_class = icon_map.get(freshness, ("?", "unknown-icon"))
        result_text = freshness.capitalize()

        st.markdown(f"""
        <div class="card" style="min-height: 400px;">
          <h2 class="card-title">Classification Results</h2>
          <div class="result-card">
            <div class="result-header">
              <div class="result-icon {icon_class}">{icon_symbol}</div>
              <div>
                <h3 class="result-title">{result_text}</h3>
                <p class="result-subtitle">{conf}% confidence</p>
              </div>
            </div>
            <h4 class="detail-section-title">Analysis Details</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
              <div class="detail-box">
                <p class="detail-label">Freshness</p>
                <p class="detail-value">{result_text}</p>
              </div>
              <div class="detail-box">
                <p class="detail-label">Confidence</p>
                <p class="detail-value">{conf}%</p>
              </div>
            </div>
            <div class="detail-box">
              <p class="detail-label">Recommendation</p>
              <p class="detail-value">
                {"Good to eat! 🍏" if freshness=="fresh" else
                 "Still okay, but consume soon. 🍌" if freshness=="mild" else
                 "Not recommended. 🚫"}
              </p>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)



# Footer
st.markdown("""
<div class="footer">
    © 2025 FreshFruit AI • Powered by Streamlit
</div>
""", unsafe_allow_html=True)