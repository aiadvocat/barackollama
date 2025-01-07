import streamlit as st
import requests
import json
from pathlib import Path

# Get the path to the assets directory
ASSETS_DIR = Path(__file__).parent / "assets"

# Configure Streamlit page
st.set_page_config(
    page_title="Barack Ollama",
    page_icon=str(ASSETS_DIR / "ObamaLaugh.png"),
    layout="wide"
)

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/chat"

def get_image_base64():
    """Convert the image to base64 for inline display"""
    import base64
    image_path = ASSETS_DIR / "ObamaLaugh.png"
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def initialize_session_state():
    """Initialize all session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'system_prompt' not in st.session_state:
        st.session_state.system_prompt = "You are Barack Ollama, a helpful AI assistant."
    if 'temp_prompt' not in st.session_state:
        st.session_state.temp_prompt = st.session_state.system_prompt

def query_ollama(messages):
    """
    Send a query to the Ollama API and get the response
    """
    # Add system prompt as the first message if messages list is not empty
    if messages:
        full_messages = [
            {"role": "system", "content": st.session_state.system_prompt}
        ] + messages
    else:
        full_messages = messages

    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": "llama3",
                "messages": full_messages,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()['message']['content']
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with Ollama: {str(e)}")
        return None

def display_chat_history():
    """Display all messages in the chat history"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def update_system_prompt(prompt):
    """Callback function to update system prompt"""
    st.session_state.system_prompt = prompt
    # Store the prompt separately for the text area
    st.session_state.temp_prompt = prompt

def settings_tab():
    """Contents of the settings tab"""
    st.title("Settings ⚙️")
    
    # System Prompt Configuration
    st.header("System Prompt")
    st.info("The system prompt helps set the behavior and context for the AI assistant.")
    
    # Use the temp_prompt for the text area value
    new_system_prompt = st.text_area(
        "Customize the system prompt:",
        value=st.session_state.temp_prompt,
        height=150,
        key="system_prompt_input",
        help="This prompt will be sent with every message to guide the AI's behavior."
    )

    if st.button("Update System Prompt"):
        update_system_prompt(new_system_prompt)
        st.success("System prompt updated successfully!")

    # Add example prompts
    st.header("Example System Prompts")
    example_prompts = {
        "Default Assistant": "You are Barack Ollama, a helpful AI assistant.",
        "Professional Expert": "You are a professional expert focused on providing accurate, detailed, and well-researched information.",
        "Creative Writer": "You are a creative writing assistant, skilled in storytelling and generating imaginative content.",
        "Barack Obama": "You are Barack Obama, the 44th President of the United States. You are a helpful and knowledgeable assistant who can answer questions about your life, presidency, and the world at large.",
        "Douglas Adams": "You are Douglas Adams, the author of The Hitchhiker's Guide to the Galaxy. You are a helpful and knowledgeable assistant who can answer questions about your books, life, and the world at large."
    }

    # Use columns to arrange buttons in a grid
    cols = st.columns(2)
    for idx, (title, prompt) in enumerate(example_prompts.items()):
        with cols[idx % 2]:
            if st.button(f"Use {title} Prompt", key=f"btn_{title}"):
                update_system_prompt(prompt)
                st.rerun()  # Force a rerun to update the text area

def chat_tab():
    """Contents of the main chat tab"""
    # Set up the page structure with CSS
    st.markdown("""
        <style>
        .stChatFloatingInputContainer {
            position: sticky !important;
            bottom: 0;
            background: transparent !important;
        }
        .stChatContainer {
            padding-bottom: 5rem;
        }
        .title-image {
            height: 2.5em;
            vertical-align: middle;
            margin-left: 0.1em;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with inline image
    st.markdown(
        f'<h1>Barack Ollama <img src="data:image/png;base64,{get_image_base64()}" class="title-image"></h1>',
        unsafe_allow_html=True
    )
    st.subheader("Your AI Assistant powered by Ollama")

    # Display chat history
    display_chat_history()

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = query_ollama(st.session_state.messages)
                if response:
                    st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.rerun()

def main():
    initialize_session_state()

    # Sidebar
    if st.sidebar.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    # Display information about the chat in the sidebar
    st.sidebar.title("Chat Information")
    st.sidebar.info(
        """
        This chatbot uses Ollama running locally on port 11434.
        
        Current Settings:
        - Model: llama3
        - Messages in conversation: {}
        """.format(len(st.session_state.messages))
    )

    # Create tabs
    tab1, tab2 = st.tabs(["Chat", "Settings"])
    
    with tab1:
        chat_tab()
    
    with tab2:
        settings_tab()

if __name__ == "__main__":
    main() 