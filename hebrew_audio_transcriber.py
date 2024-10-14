import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

def transcribe_audio(directory):
    recognizer = sr.Recognizer()
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(('.wav', '.mp3', '.flac')):
                continue

            audio_path = os.path.join(root, file)
            text_path = os.path.splitext(audio_path)[0] + '.txt'

            if os.path.exists(text_path):
                print(f"Text file already exists for {file}, skipping transcription.")
                continue

            try:
                # Convert non-WAV files to WAV format
                if not file.endswith('.wav'):
                    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_wav:
                        audio = AudioSegment.from_file(audio_path)
                        audio.export(temp_wav.name, format='wav')
                        audio_path = temp_wav.name

                with sr.AudioFile(audio_path) as source:
                    print(f"Transcribing {file}...")
                    audio_data = recognizer.record(source)
                    text = recognizer.recognize_google(audio_data, language='he')
                    
                    with open(text_path, 'w', encoding='utf-8') as f:
                        f.write(text)
                    print(f"Transcription completed for {file}.")
            except Exception as e:
                print(f"Failed to transcribe {file}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path to search for audio files: ")
    transcribe_audio(directory)