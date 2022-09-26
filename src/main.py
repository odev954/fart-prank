import ctypes
import sys
import os
from winevt import EventLog
from WinCodes import SW, ERROR
from AudioPlayer import AudioPlayer

directory = os.path.dirname(__file__)

PLAYER = AudioPlayer(directory + '/audios')

def handle_event(action, context_pointer, event):
    """
    handler for windows event.
    """
    PLAYER.play_next()

def bootstrap():
    """
    bootstraps the script with administrative privileges.
    """
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
        hinstance = ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, sys.argv[0], None, SW.HIDE
        )
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))

def main():
    EventLog.Subscribe("Security","Event/System[EventID=4688]", handle_event)
    os.system("pause")

if __name__ == '__main__':
    bootstrap()
