#!/usr/bin/env python3

import wave
import sys

from vosk import Model, KaldiRecognizer, SetLogLevel
import json

# You can set log level to -1 to disable debug messages
SetLogLevel(0)
MODEL_PATH="./vosk-model-ja-0.22"
# wf = wave.open(sys.argv[1], "rb")

class MyVosk():
    def TextConvert(file):
        wf = wave.open(file, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format mono PCM.")
            sys.exit(1)

        # model = Model(lang="ja")
        model = Model(model_path=MODEL_PATH)

        # You can also init model by name or with a folder path
        # model = Model(model_name="vosk-model-en-us-0.21")
        # model = Model("models/en")

        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        rec.SetPartialWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                rec.Result()
            else:
                rec.PartialResult()

        final = rec.FinalResult()
        # print(final)
        print(json.loads(final)['text'])
        return(json.loads(final)['text'])
