from youtube_transcript_api import YouTubeTranscriptApi
import g4f
import customtkinter as ctk


## -- Split the url id  --
def get_video_id(url_yt): 
    return url_yt.split("watch?v=")[-1]

## -- Input the url  --
url = input("Past your YouTube URL here: ")
video_id = get_video_id(url)

## -- transcribing the video in these languages --
transcipt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en','pt','es']) 

## -- Merge the all text --
transcipt_joined = " ".join([line['text'] for line in transcipt])

## -- AI to summary the video --
def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4o,
        messages=messages
    )
    print(response)
    return response

messages = [
    {"role": "user", "content": f"Resuma em tópicos essa transcrição do vídeo do YouTube na linguagem que estiver escrita:\n\n{transcipt_joined}"}
]

## -- Enviar ao modelo e mostrar o resultado --
resposta = ask_gpt(messages)
print("\n📋 Resumo em tópicos:\n")
print(resposta)

