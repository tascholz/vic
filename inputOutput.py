import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio
import json

class Input():
	def __init__(self):
		self.model = Model(r'./models/vosk-model-small-de-0.15')
		self.recognizer = KaldiRecognizer(self.model, 16000)
		self.cap = pyaudio.PyAudio()
		self.stream = self.cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
		self.stream.start_stream()

	def listen(self):
		while True:
			data = self.stream.read(4096, exception_on_overflow=False)

			if len(data) == 0:
				break

			if self.recognizer.AcceptWaveform(data):
				result = json.loads(self.recognizer.Result())["text"]
				return result


class OAudio():
	def __init__(self):
		self.engine = pyttsx3.init()

	def say(self, phrase):
		self.engine.say(phrase)
		self.engine.runAndWait()


