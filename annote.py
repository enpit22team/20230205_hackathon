from dotenv import load_dotenv
from pyannote.audio import Pipeline

load_dotenv()
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1")
print(pipeline)
diarization = pipeline("data/sample.wav")

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")