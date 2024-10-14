# Hebrew Audio Transcriber

This project provides a Python script that transcribes Hebrew audio files into text. The script will skip transcribing files that already have a corresponding text file with the same name.

## Features
- Supports `.wav`, `.mp3`, and `.flac` audio formats.
- Automatically transcribes Hebrew audio files in a user-specified directory.
- Skips audio files that already have a matching transcription text file.

## Requirements

- Python 3.6+
- Required Python packages:
  - `SpeechRecognition`
  - `pydub`

To install the required packages, run:
```bash
pip install SpeechRecognition pydub
```

You will also need **ffmpeg** to handle non-wav audio formats. You can install it via:
- [Windows](https://ffmpeg.org/download.html)
- [MacOS](https://ffmpeg.org/download.html) (using Homebrew: `brew install ffmpeg`)
- [Linux](https://ffmpeg.org/download.html)

## Usage

Run the script and provide the directory path containing the audio files to be transcribed:

```bash
python hebrew_audio_transcriber.py
```

