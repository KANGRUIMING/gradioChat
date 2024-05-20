# Gradio Voiceover Transcription Program

This program uses Gradio to create an interface for transcribing audio input and generating voiceover responses using OpenAI's GPT-3.5-turbo and ElevenLabs' text-to-speech API.

## Features
- Transcribe audio input using OpenAI's Whisper model.
- Generate voiceover responses using ElevenLabs' text-to-speech API.
- Interactive Gradio interface for easy use.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```
2. Install the required packages:
   ```bash
   pip install gradio openai pydub requests numpy ipython python-magic

   ```
3. Set up the configuration:
Create a config.py file with your API keys:
OPENAI_API_KEY = 'your_openai_api_key'
ElevenLabs_API_KEY = 'your_elevenlabs_api_key'

## Usage
1. Run the program:
  ```bash
   python app.py
   ```
2. Open the Gradio interface in your browser and start speaking.

## Code Overview
- Generate_voiceover(content): Generates a voiceover from the provided text content using ElevenLabs' API.
- Transcribe(audio): Transcribes the provided audio file using OpenAI's Whisper model and generates a conversation transcript.


   
