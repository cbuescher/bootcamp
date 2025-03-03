import librosa
from panns_inference import AudioTagging
import numpy as np
from logs import LOGGER

def get_audio_embedding(path):
    # Use panns_inference model to generate feature vector of audio
    try:
        audio, _ = librosa.core.load(path, sr=32000, mono=True)
        audio = audio[None, :]
        at = AudioTagging(checkpoint_path=None, device='cuda')
        _, embedding = at.inference(audio)
        embedding = embedding/np.linalg.norm(embedding)
        embedding = embedding.tolist()[0]
        return embedding
    except Exception as e:
        LOGGER.error(f"Error with embedding:{e}")
        return None
