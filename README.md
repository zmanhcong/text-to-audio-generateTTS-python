# Text-to-Speech (TTS) Vocabulary Learning Tool

This repository contains a Python script designed to assist in language learning through the creation of custom Text-to-Speech (TTS) audio files. The script generates spoken versions of vocabulary words, their examples, and meanings, facilitating auditory learning.

## What is TTS: Text to Speech in this Repository

The Text to Speech (TTS) functionality in this repository allows users to convert a list of vocabulary words, along with their example sentences and meanings, into an audio file. This can be particularly useful for language learners who wish to improve their pronunciation and listening skills.

## ⭐ Key Features

- **Vocabulary Audio Generation**: Convert text files containing vocabulary words, example sentences, and meanings into spoken audio.
- **Customizable Speed and Silence**: Adjust the speed of the spoken text and the duration of silence between words for better comprehension.
- **Support for Multiple Languages**: While primarily focused on English and Vietnamese, the script can be adapted for other languages supported by Google's Text-to-Speech API.

## 📀 Installation

To use this TTS tool, you will need Python installed on your computer. Additionally, you will need to install the following Python packages:

```bash
pip install gtts pydub
```

※Note: pydub requires ffmpeg or avlib. Please ensure one of these is installed and available in your system's PATH.

## 🐍 Usage in Python

1. Prepare your vocabulary list in a text file (list.txt) with each line formatted as: word/example sentence/meaning.

2. Place the text file in the same directory as the script.

3. Run the script:

```bash
python GenerateTTS.py
```

4. The script will generate an MP3 file (all_vocabulary.mp3) in the 'audio' directory, containing the synthesized speech of your vocabulary list.
