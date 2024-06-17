from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy
import os

MODEL = 'facebook/musicgen-small'
def generate_song(prompt):
    print("")
    print(f'Generating song using prompt: {prompt}')
    print("")
    directory = 'generated_songs'
    if not os.path.exists(directory):
        os.makedirs(directory)
    processor = AutoProcessor.from_pretrained(MODEL)
    model = MusicgenForConditionalGeneration.from_pretrained(MODEL)

    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors='pt',
    )

    audio_values = model.generate(**inputs, max_new_tokens=800)

    sampling_rate = model.config.audio_encoder.sampling_rate

    path = f'{directory}/song.wav'
    scipy.io.wavfile.write(path, rate=sampling_rate, data=audio_values.numpy())
    return path