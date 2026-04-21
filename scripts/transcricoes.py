from youtube_transcript_api import YouTubeTranscriptApi
import csv
import re

# =========================
# LISTA DE VÍDEOS
# =========================
video_ids = [
    "u321m25rKXc", #456
    "Rz-4ulRKnz4", #457
    "8NLzc9kobDk", #453
    "Q8Qk_3a3lUw", #445
    "qCbfTN-caFI", #442
    "QJtPROVsePk", #441
    "2oxdDKHdcM8", #436
    "_El9riy9Zjw", #423
    "0cn3VBjfN8g"  #422
    # adicione mais IDs aqui
]

# =========================
# INICIALIZA API
# =========================
ytt_api = YouTubeTranscriptApi()

# =========================
# FUNÇÃO DE LIMPEZA
# =========================
def limpar_texto(texto):
    texto = re.sub(r"\s+", " ", texto)        # remove espaços extras
    texto = re.sub(r"\[.*?\]", "", texto)     # remove [música], [aplausos], etc
    return texto.strip()

# =========================
# PROCESSAMENTO
# =========================
for video_id in video_ids:
    print(f"\nProcessando vídeo: {video_id}")

    try:
        transcript = ytt_api.fetch(video_id)

        # cria um CSV para cada vídeo
        with open(f"{video_id}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # cabeçalho (compatível com seu NER)
            writer.writerow(["text"])

            linhas_validas = 0

            for t in transcript:
                texto_limpo = limpar_texto(t.text)

                # evita textos muito curtos (ruído)
                if len(texto_limpo) > 3:
                    writer.writerow([texto_limpo])
                    linhas_validas += 1

        print(f"{video_id}.csv salvo ({linhas_validas} linhas)")

    except Exception as e:
        print(f"Erro no vídeo {video_id}: {e}")

print("\n--- FINALIZADO ---")