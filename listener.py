import sounddevice as sd
import wave


def record_audio(filename="recording.wav", duration=5):
    sample_rate = 16000

    print("V.A.N.T.A.: Listening...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    with wave.open(filename, "wb") as audio_file:
        audio_file.setnchannels(1)
        audio_file.setsampwidth(2)
        audio_file.setframerate(sample_rate)
        audio_file.writeframes(audio.tobytes())

    print("V.A.N.T.A.: Recording saved.")
    return filename
