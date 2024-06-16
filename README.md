# GrooveMatch

Search for your favorite song and then let AI generate new ones that are similar!

# Technology
* [MusicGen](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md) - Meta AI's text-to-music model (via the [Hugging Face Transfomers](https://github.com/huggingface/transformers) library) - Used to generate song samples.
* [OpenAI API](https://platform.openai.com/docs/overview) - For generating text prompt that describes characteristics of original song. This prompt is passed to the MusicGen model.
* [Spotify Web API](https://developer.spotify.com/documentation/web-api) - To search for songs based on user input.
