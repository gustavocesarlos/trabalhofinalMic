import os, subprocess, yowsup, logging
from wasend import YowsupSendStack
#from wareceive import YowsupReceiveStack, MessageReceived

def credential():
    return "5519983630573","=VDdLcMfAkKV+TPxNOv+cRIoC7/M="

def Answer():
    try:
        stack=YowsupSendStack(credential(), ["5512981213965", "saida.png"])
        stack.start()
    except:
        pass
    return
