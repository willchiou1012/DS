from TTS.api import TTS
import IPython.display as ipd

tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=True)

text = "你好，今天飼料補充的次數總共為2次"
tts.tts_to_file(text=text, file_path="output.wav")

ipd.display(ipd.Audio("output.wav"))
