import os, subprocess, yowsup, logging
from wasend import YowsupSendStack
#from wareceive import YowsupReceiveStack, MessageReceived

def credential():
    return "55XXXXXXXXXXX","=VDdLcMfAkKVXXXXXXXXXXXXXXXX="

def Answer():
    try:
        stack=YowsupSendStack(credential(), ["55XXXXXXXXXXX", "saida.png"])
        stack.start()
    except:
        pass
    return
