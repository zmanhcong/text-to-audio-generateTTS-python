from gtts import gTTS
from pydub import AudioSegment
import os

def create_silence(duration_ms=1000):
    """Creates a silence of the specified duration."""
    return AudioSegment.silent(duration=duration_ms)

def change_speed(sound, speed=1.0):
    """Change the speed of the audio track."""
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def read_vocabulary_list(file_path):
    """Read vocabulary list from file."""
    vocabulary_list = []
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('/')
            if len(parts) == 3:
                vocabulary_list.append({"word": parts[0], "example": parts[1], "meaning": parts[2]})
    return vocabulary_list

# Path to file list
list_file_path = './list.txt'

vocabulary_list = read_vocabulary_list(list_file_path)

# Make sure the audio directory exists
audio_dir = "audio"
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)

combined_audio = AudioSegment.empty()

for vocab in vocabulary_list:
    # Check and create audio for the word if there is content
    if vocab["word"].strip():
        tts_word = gTTS(text=vocab["word"], lang='en', slow=False)
        word_path = f"{audio_dir}/temp_word.mp3"
        tts_word.save(word_path)
        combined_audio += AudioSegment.from_mp3(word_path) + create_silence(2000)
    
    # Check and create audio for the example, read slower if there is content
    if vocab["example"].strip():
        tts_example = gTTS(text=vocab["example"], lang='en', slow=True)
        example_path = f"{audio_dir}/temp_example.mp3"
        tts_example.save(example_path)
        example_audio = AudioSegment.from_mp3(example_path)
        slowed_example_audio = change_speed(example_audio, speed=1)
        combined_audio += slowed_example_audio + create_silence(2000)

    # Check and create audio for Vietnamese meaning if there is content
    if vocab["meaning"].strip():
        tts_meaning = gTTS(text=vocab["meaning"], lang='vi', slow=False)
        meaning_path = f"{audio_dir}/temp_meaning.mp3"
        tts_meaning.save(meaning_path)
        combined_audio += AudioSegment.from_mp3(meaning_path) + create_silence(2000)



combined_audio.export(f"{audio_dir}/all_vocabulary.mp3", format="mp3")

os.remove(word_path)
os.remove(example_path)
os.remove(meaning_path)

print("The synthetic audio file has been created.")

