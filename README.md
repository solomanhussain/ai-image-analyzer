# AI Image Analyzer

A Streamlit application that uses Ollama's LLaVA model to analyze images and generate descriptive keywords. The application can identify visual elements, detect text in images, and provide comprehensive descriptions through AI analysis.

## Features

- 🖼️ Image Analysis: Upload and analyze images using AI
- 📝 Text Detection: Automatically identifies and extracts text from images
- 🎯 Keyword Generation: Creates detailed, comma-separated keywords describing the image
- ⚙️ Configurable Settings: Customize Ollama URL and model selection
- 🎨 User-friendly Interface: Clean, intuitive web interface built with Streamlit

## Prerequisites

- Python 3.6+
- Ollama installed and running locally
- LLaVA model pulled in Ollama

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-image-analyzer
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Ollama is running with LLaVA model:
```bash
ollama pull llava
```

## Usage

1. Start the application:
```bash
streamlit run Home.py
```

2. Access the web interface at `http://localhost:8501`

3. Configure settings:
   - Click on "Settings" in the sidebar
   - Set your Ollama URL (default: http://localhost:11434)
   - Select your model (default: llava)

4. Analyze images:
   - Navigate to "Image Analyzer" in the sidebar
   - Upload an image (supported formats: JPG, JPEG, PNG)
   - View the generated keywords and analysis

## Application Structure

```
.
├── Home.py               # Main application entry point (Home page)
├── pages/
│   ├── 01_Settings.py    # Configuration page
│   └── 02_Image_Analyzer.py # Image analysis page
└── requirements.txt       # Python dependencies
```

## Configuration

The application allows configuration of:
- Ollama API URL
- Model selection
- Settings are persisted across sessions

## Output Format

The analysis results are provided as a comma-separated list of keywords that include:
- Visual elements and objects
- Colors and textures
- Text detected in the image
- Mood and atmosphere
- Setting and context

## Error Handling

The application includes robust error handling for:
- Image upload issues
- API connection problems
- Model execution errors
- File system operations

## Tips for Best Results

1. Use clear, well-lit images
2. Ensure images are in supported formats (JPG, JPEG, PNG)
3. Check Ollama connection if analysis fails
4. Verify model availability in Ollama

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]