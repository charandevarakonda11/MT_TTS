from gtts import gTTS

telugu_text = "సున్నా సున్నా అయిదు ఏడు ఎనిమిది"

tts = gTTS(text=telugu_text, lang='te', slow=False)

tts.save("telugu_output.mp3")

print("Audio saved as telugu_output.mp3")
