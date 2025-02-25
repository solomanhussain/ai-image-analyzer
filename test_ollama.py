import requests

def test_ollama_api():
    """Test if Ollama API is responsive"""
    try:
        # Simple test query to Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llava",
                "prompt": "Hello, are you working?",
                "stream": False
            }
        )
        
        if response.status_code == 200:
            print("✅ Ollama API is working!")
            print("\nResponse:", response.json()["response"])
        else:
            print("❌ Error:", response.status_code)
            print("\nResponse:", response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama API. Is the server running?")
    except Exception as e:
        print("❌ Unexpected error:", str(e))

if __name__ == "__main__":
    print("Testing Ollama API connection...")
    test_ollama_api()