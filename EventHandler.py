import threading
import time

class EventHandler:
    def __init__(self, sp, onNextTrack=None, onCommand=None):
        self.sp = sp
        self.currentTrack = sp.currently_playing()
        self.onNextTrack = onNextTrack
        self.onCommand = onCommand

        nextTrackThread = threading.Thread(target=self.nextTrackHook, args=())
        commandThread = threading.Thread(target=self.commandHook, args=())

        nextTrackThread.start()
        commandThread.start()

    def nextTrackHook(self):
        while True:
            currentTrack = self.sp.currently_playing()

            if currentTrack != None and self.currentTrack != None and currentTrack['item'] != self.currentTrack['item']:
                if self.onNextTrack != None:
                    self.onNextTrack()

            self.currentTrack = currentTrack

            time.sleep(0.5)

    def commandHook(self):
        while True:
            command = input('$ ')

            if self.onCommand != None:
                args = command.split(' ')
                self.onCommand(args)
