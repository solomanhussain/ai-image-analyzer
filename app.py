"""
Main entry point for the AI Image Analyzer Streamlit application.
"""
import streamlit as st

def main():
    st.set_page_config(
        page_title="AI Image Analyzer",
        page_icon="🖼️",
        layout="wide"
    )

    st.title("🖼️ Welcome to AI Image Analyzer")
    
    st.markdown("""
    Welcome to the AI Image Analyzer! This application helps you analyze images using AI to generate descriptive keywords.
    
    ### Getting Started
    1. Click on 'Image Analyzer' in the sidebar to start analyzing images
    2. Use 'Settings' to configure the Ollama URL and model
    
    ### Features
    - Generate detailed keywords from images
    - Detect and extract text from images
    - Configurable AI model settings
    - Easy-to-use interface
    """)

if __name__ == "__main__":
    main()