import ffmpeg
import speech_recognition


def speech2text(path : str) -> str:
    """
    mp4ファイルからテキスト抽出を行う

    Parameters
    ----------
    path: str
        動画ファイルのパス
    
    Returns
    -------
    text: str
        抽出結果
    """
    outwav = "./data/sample.wav"
    # mp4 to wav
    stream = ffmpeg.input(path)
    stream = ffmpeg.output(stream, outwav)
    ffmpeg.run(stream, overwrite_output=True, quiet=True)

    r = speech_recognition.Recognizer()

    with speech_recognition.AudioFile(outwav) as source:
        audio = r.record(source)
    
    text = r.recognize_google(audio, language="ja-JP")

    return text


if __name__ == '__main__':
    txt = speech2text("data/min_ten.mp4")
    print(txt)