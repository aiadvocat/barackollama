# Barack Ollama <img src="src/assets/ObamaLaugh.png" height="32px" style="vertical-align: middle;">

A Streamlit-based chat interface for Ollama, featuring Barack Obama-themed interactions. This application provides a user-friendly interface to interact with Ollama's LLM models, with customizable system prompts and persistent chat history.

## Features

- 🤖 Clean chat interface for Ollama interactions
- 💬 Multi-turn conversation support
- 🔄 Persistent chat history within sessions
- ⚙️ Customizable system prompts
- 📝 Pre-configured personality prompts (Barack Obama, Professional Expert, etc.)
- 🎨 Dark mode compatible
- 📊 Chat statistics in sidebar

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally on port 11434
- The llama3 model pulled in Ollama

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/barack-ollama.git
   cd barack-ollama
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure Ollama is running locally:
   ```bash
   ollama serve
   ```

2. In a new terminal, make sure you have the llama3 model:
   ```bash
   ollama pull llama3
   ```

3. Start the Streamlit application:
   ```bash
   streamlit run src/app.py
   ```

The application will open in your default web browser at `http://localhost:8501`.

## Usage

1. **Chat Interface**: Use the main chat tab to interact with the AI. Type your messages in the input field at the bottom.

2. **System Prompts**: Switch to the Settings tab to customize the AI's behavior:
   - Use pre-configured prompts (Barack Obama, Professional Expert, etc.)
   - Create your own custom system prompt
   - Update the prompt at any time during conversation

3. **Chat Management**:
   - Clear chat history using the button in the sidebar
   - View current conversation statistics in the sidebar

## Project Structure

```
barack-ollama/
├── src/
│   ├── assets/
│   │   └── ObamaLaugh.png
│   ├── app.py
│   └── components/
├── requirements.txt
├── README.md
└── .gitignore
```

## Dependencies

- streamlit>=1.27.0
- pandas>=2.0.0
- numpy>=1.24.0
- requests>=2.31.0

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.