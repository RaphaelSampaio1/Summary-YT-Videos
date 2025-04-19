import customtkinter as ctk
from youtube_transcript_api import YouTubeTranscriptApi
import g4f



# Configurações de estilo
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Janela principal
app = ctk.CTk()
app.geometry("700x600")
app.title("Resumo de Vídeo do YouTube")
app.configure(bg="#010409")

# Função para extrair ID
def get_video_id(url_yt): 
    return url_yt.split("watch?v=")[-1]

# Função para perguntar ao GPT
def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4o,
        messages=messages
    )
    return response

# Função principal
def gerar_resumo():
    url = entry_url.get()
    if not url:
        textbox_resultado.insert("0.0", "Por favor, insira uma URL válida.")
        return

    textbox_resultado.delete("0.0", "end")
    textbox_resultado.insert("0.0", "🔄 Processando...\n")

    try:
        video_id = get_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en','pt','es'])
        transcript_joined = " ".join([line['text'] for line in transcript])
        
        messages = [
            {"role": "user", "content": f"Resuma em tópicos essa transcrição do vídeo do YouTube na linguagem que estiver escrita:\n\n{transcript_joined}"}
        ]

        resposta = ask_gpt(messages)
        textbox_resultado.delete("0.0", "end")
        textbox_resultado.insert("0.0", f"📋 Resumo em tópicos:\n\n{resposta}")

    except Exception as e:
        textbox_resultado.delete("0.0", "end")
        textbox_resultado.insert("0.0", f"❌ Erro: {str(e)}")

# Elementos da Interface
entry_url = ctk.CTkEntry(app, width=600, placeholder_text="Cole aqui a URL do vídeo do YouTube", fg_color="#28303b", text_color="#f0f6fc")
entry_url.pack(pady=20)

btn_resumir = ctk.CTkButton(app, text="Gerar Resumo", command=gerar_resumo, fg_color="#28303b", text_color="#f0f6fc", hover_color="#3c4859")
btn_resumir.pack(pady=10)

textbox_resultado = ctk.CTkTextbox(app, width=650, height=400, fg_color="#28303b", text_color="#f0f6fc", font=("Arial", 14))
textbox_resultado.pack(pady=10)

# Inicia o app
app.mainloop()
