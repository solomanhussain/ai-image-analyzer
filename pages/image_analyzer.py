"""
Streamlit interface for AI Image Analysis using Ollama's LLaVA model.
"""
import io
import base64
from pathlib import Path
import streamlit as st
from PIL import Image
import requests

def analyze_image(image_path):
    """
    Analyze image using Ollama's LLaVA model and return the description.
    """
    try:
        # Read and encode image
        with open(image_path, "rb") as f:
            image_bytes = f.read()
            base64_image = base64.b64encode(image_bytes).decode()

        # Prepare the prompt to generate clean keyword list
        prompt = """Analyze this image and provide a comma-separated list of descriptive keywords and phrases. Pay special attention to:
- any text or words visible in the image (exactly as written)
- objects and people in the scene
- colors, lighting, and visual details
- setting and environment
- overall mood and style

Important:
- Include ALL text visible in the image exactly as written
- Provide ONLY keywords separated by commas
- Do not include category labels or classifications

Example format: "Sale 50% off", modern storefront, red signage, glass windows, bright lighting, urban setting, busy street

Your response should be a single line of comma-separated keywords with any visible text quoted."""
        
        # Call Ollama API
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llava",
                "prompt": prompt,
                "images": [base64_image],
                "stream": False
            }
        )
        
        if response.status_code == 200:
            return response.json()["response"]
        else:
            st.error(f"Error analyzing image: {response.text}")
            return None
    except Exception as e:
        st.error(f"Error in analyze_image: {str(e)}")
        return None

def save_uploaded_file(uploaded_file):
    """Save uploaded file temporarily and return the path."""
    temp_path = Path("temp_image.jpg")
    try:
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        return temp_path
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="AI Image Analyzer",
        page_icon="🖼️",
        layout="wide"
    )

    st.title("🖼️ AI Image Keyword Generator")
    st.markdown("""
    Upload an image to get a comprehensive list of descriptive keywords using AI analysis.
    The AI will analyze every aspect of your image and provide detailed keywords.
    """)

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        help="Upload an image file (JPG or PNG)"
    )

    if uploaded_file:
        # Display the uploaded image
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Uploaded Image")
            try:
                image = Image.open(uploaded_file)
                # Convert to RGB if needed
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                st.image(image, use_container_width=True)  # Updated parameter name
                
                # Save file and analyze
                temp_path = save_uploaded_file(uploaded_file)
                if temp_path:
                    with col2:
                        st.subheader("Analysis Results")
                        
                        with st.spinner("Analyzing image..."):
                            description = analyze_image(temp_path)
                            if description:
                                st.markdown("### Image Keywords")
                                st.write(description)
                    
                    # Clean up temporary file
                    if temp_path.exists():
                        temp_path.unlink()
            
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()