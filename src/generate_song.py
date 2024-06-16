from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy

MODEL = 'facebook/musicgen-small'
def generate_song(prompt):
    print("")
    print(f'Generating song using prompt: {prompt}')
    print("")
    processor = AutoProcessor.from_pretrained(MODEL)
    model = MusicgenForConditionalGeneration.from_pretrained(MODEL)

    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors='pt',
    )

    audio_values = model.generate(**inputs, max_new_tokens=800)
    print(audio_values)

    sampling_rate = model.config.audio_encoder.sampling_rate
    scipy.io.wavfile.write('generated_songs/song.wav', rate=sampling_rate, data=audio_values.numpy())