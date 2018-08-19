import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

print(sr.Microphone.list_microphone_names())

with mic as source:
    # param language='cn'?
    # duration control recording
    print("i'm listening....")
    audio = r.listen(source)

result = r.recognize_bing(audio, key='8a852346d53e4d90bbad11594c01fb85',language='zh-cn')
print(result)
