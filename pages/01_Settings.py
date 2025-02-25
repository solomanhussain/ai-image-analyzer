"""
Configuration page for AI Image Analyzer settings.
"""
import streamlit as st

def main():
    st.set_page_config(
        page_title="AI Image Analyzer Settings",
        page_icon="⚙️",
        layout="wide"
    )

    st.title("⚙️ Configuration Settings")
    
    # Initialize session state for settings if not exists
    if "ollama_url" not in st.session_state:
        st.session_state.ollama_url = "http://localhost:11434"
    if "model_name" not in st.session_state:
        st.session_state.model_name = "llava"

    st.markdown("""
    Configure the connection settings for the AI Image Analyzer.
    These settings will be used for all image analysis operations.
    """)

    # Configuration form
    with st.form("config_form"):
        # Ollama URL setting
        ollama_url = st.text_input(
            "Ollama API URL",
            value=st.session_state.ollama_url,
            help="The URL where Ollama is running (default: http://localhost:11434)"
        )

        # Model selection
        model_name = st.text_input(
            "Model Name",
            value=st.session_state.model_name,
            help="The name of the model to use for image analysis (default: llava)"
        )

        # Save button
        if st.form_submit_button("Save Settings"):
            st.session_state.ollama_url = ollama_url
            st.session_state.model_name = model_name
            st.success("Settings saved successfully!")

    # Display current settings
    st.markdown("### Current Settings")
    st.info(f"""
    - **Ollama API URL**: {st.session_state.ollama_url}
    - **Model Name**: {st.session_state.model_name}
    """)

if __name__ == "__main__":
    main()