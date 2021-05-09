#!/bin/python3

from vidstream import *
import tkinter as tk
import threading

localIpAddress = "0.0.0.0"
server = StreamingServer(localIpAddress, 4444)
receiver = AudioReceiver(localIpAddress, 7777)

#Functions

def startListening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
def startCamera():
    camClient = CameraClient(textTargetIp.get(1.0,'end-1c'), 8888)
    t3 = threading.Thread(target=camClient.start_stream)
    t3.start()
def screenSharing():
    scrnShare = ScreenShareClient(textTargetIp.get(1.0,'end-1c'), 8888)
    t4 = threading.Thread(target=scrnShare.start_stream)
    t4.start()
def audioStream():
    audio = AudioSender(textTargetIp.get(1.0,('end-1c'), 6666))
    t5 = threading.Thread(target=audio.start_stream)
    t5.start()

#GUI

window = tk.Tk()
window.title("Video Call Client v0.0.1")
window.geometry('300x200')

textTargetIp = tk.Label(window, text="Target IP : ")
textTargetIp.pack()

targetIpInput = tk.Text(window, height=1)
targetIpInput.pack()

startListeningBtn = tk.Button(window, text="Start Listening/Waiting for calls", width=50, command=startListening)
startListeningBtn.pack(anchor=tk.CENTER, expand=True)

startScreenSharingBtn = tk.Button(window, text="Start Screen Sharing", width=50, command=screenSharing)
startScreenSharingBtn.pack(anchor=tk.CENTER, expand=True)

startCameraStream = tk.Button(window, text="Start Streaming Video from camera", width=50, command=startCamera)
startCameraStream.pack(anchor=tk.CENTER, expand=True)

startAudioStream = tk.Button(window, text="Start Audio stream through mic", width=50, command=startAudioStream)
startAudioStream.pack()

window.mainloop()
