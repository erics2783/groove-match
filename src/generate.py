from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy

MODEL = 'facebook/musicgen-small'
def generate(prompt):
    print(f'generating song using prompt: {prompt}')
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