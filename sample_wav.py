import ffmpeg
import speech_recognition
import torch
import whisper

inputfile = "./data/sample.mp4"
outputfile = "./data/sample.wav"

r = speech_recognition.Recognizer()

# stream = ffmpeg.input(inputfile)
# stream = ffmpeg.output(stream, outputfile)
# ffmpeg.run(stream)

with speech_recognition.AudioFile(outputfile) as source:
    audio = r.record(source)

text = r.recognize_google(audio, language="ja-JP")
print(text)
# model = whisper.load_model("base")

# result = model.transcribe(outputfile, language="ja", fp16=False)

# print(result["text"])