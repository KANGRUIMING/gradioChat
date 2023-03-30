

import gradio as gr
import openai, subprocess
from pydub import AudioSegment
from pydub.playback import play
import requests
import json
from IPython.display import Audio
import numpy as np
import os
import io
import magic
from config import OPENAI_API_KEY, ElevenLabs_API_KEY

MODEL_PROMPT = "input prompt here " #@param{type: "string"}
config = {
    "api_key":OPENAI_API_KEY,
    "xi-api-key":ElevenLabs_API_KEY,
    "initial_prompt":MODEL_PROMPT
}



openai.api_key = config['api_key']

def generate_voiceover(content):
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"
    headers = {
        "accept" : "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": config['xi-api-key']
    }
    payload = {
        "text": content,
        "voice_settings":{
            "stability": 0.9,
            "similarity_boost": 1
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        audio_bytes = io.BytesIO(response.content)
        audio_segment = AudioSegment.from_file(audio_bytes)
        sample_rate = audio_segment.frame_rate
        audio_array = np.array(audio_segment.get_array_of_samples())
        audio_tuple = (sample_rate, audio_array)
        return audio_tuple
    else:
        raise Exception("Failed to generate voiceover. Status code: " + str(response.status_code))


messages = [{"role": "system", "content": config['initial_prompt']}]

def transcribe(audio):
    global messages
     
    audio = AudioSegment.from_file(audio).export("converted_audio.wav", format="wav")   
    with open("converted_audio.wav", "rb") as audio:
        transcript = openai.Audio.transcribe('whisper-1', audio)
    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    print(system_message)
    messages.append(system_message)
    print('Sending request to voiceover service')
    #voice = generate_voiceover(system_message['content'])
    print('Response received')
    chat_transcript = ""
    
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"
    
    
    return chat_transcript#, voice

    



demo = gr.Interface(
        fn=transcribe,
        inputs=gr.Audio(source="microphone", type="filepath", label = "Speak now"),
                
                
        
        outputs=["text",],#, "audio"],
        

        live = True,
        title="Input Title",
        description="Input description",
        article="When clicking 'clear', your logs are saved and will be displayed in the next response",
        allow_flagging= "never"
        )
   

demo.launch(debug = True, share=True)
