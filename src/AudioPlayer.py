import os
import playsound

class AudioPlayer():
    """
    Audio Player class.
    Plays multiple audio files for specified directory.
    """
    def __init__(self, directory_path):
        self.directory = directory_path
        self.assests = os.listdir(self.directory)
        self.picker = 0
    
    def play_next(self):
        """
        Plays the next audio file in the list.
        """
        playsound.playsound(self.directory + "/" + self.assests[self.picker % len(self.assests)], True) # pick a file
        self.picker += 1 # advance to the next audio file
