from ScriptingBridge import SBApplication
import re

iTunes = SBApplication.applicationWithBundleIdentifier_('com.apple.iTunes')
music = iTunes.sources()[0].playlists()[1]

#############################
### Convenience Functions ###
#############################
"""
    These functions could all easily be hooked into other projects to produce cool hacks
    For example, one could build a jukebox application using an API like that provided
    by Twilio or a voice remote using a speech-to-text engine
"""

# Comparator lambda and function definition for playing a specific track
trackmatch = lambda match, track: reduced(match.name()).lower() == track.lower() and match.duration() > 0
def playtrack(track):
    playmatch(track, trackmatch)

# Strips statements in brackets and parentheses out of matches for more meaningful searches
brackets = re.compile('\[[^)]*\]')
parentheses = re.compile('\([^)]*\)')
def reduced(track):
    track = re.sub(parentheses, '', track).rstrip()
    track = re.sub(brackets, '', track).rstrip()
    return track


# Comparator lambda and function definition for playing a specific artist
artistmatch = lambda match, artist: match.artist().lower() == artist.lower() and match.duration() > 0
def playartist(artist):
    playmatch(artist, artistmatch)

# Comparator lambda and function definition for playing a specific album
albummatch = lambda match, album: match.album().lower() == album.lower() and match.duration() > 0
def playalbum(album):
    playmatch(album, albummatch)

# Generic function that takes a search term and a comparator to find a matching term and play it
def playmatch(search, matchfunc):
    matches = music.searchFor_only_(search, 0)
    if matches:
        for match in matches:
            if matchfunc(match, search):
                match.playOnce_(None)
                break

####################
##### Controls #####
####################
"""
    These functions could be easily be linked with a library like BreakfastSerial 
    (https://github.com/theycallmeswift/BreakfastSerial) to build physical iTunes remotes
    with Arduinos.
"""
def playpause():
    iTunes.playpause()
def play():
    iTunes.playOnce_(None)
def pause():
    iTunes.pause()

def muteunmute():
    if iTunes.mute():
        iTunes.setMute_(False)
    else:
        iTunes.setMute_(True)
def mute():
    iTunes.setMute_(True)
def unmute():
    iTunes.setMute_(False)

def setvolume(volume):
    iTunes.setSoundVolume_(volume)
def getvolume():
    return iTunes.soundVolume()

def setposition(position):
    iTunes.setPlayerPosition_(position)
def getposition():
    return iTunes.playerPosition()

def skip():
    iTunes.nextTrack()
def back():
    iTunes.backTrack()
def prev():
    iTunes.previousTrack()

#####################
### Track Wrapper ###
#####################
"""
    These functions could be used to build temporary playlists, search for songs, etc.
"""
    
class Track():
    def __init__(self, iTunesTrack):
        self.trackid = iTunesTrack.id()
    
    def play(self):
        music.tracks().objectWithID_(self.trackid).playOnce_(None)

    def getinfo(self):
        track = music.tracks().objectWithID_(self.trackid)
        info = {
            'name': track.name(),
            'artist': track.artist(),
            'album': track.album(),
            'genre': track.genre(),
            'time': track.time(),
            'duration': track.duration()
        }
        return info


def playing():
    return Track(iTunes.currentTrack())

def search(term):
    matches = music.searchFor_only_(term, 0)
    if len(matches) == 0:
        return None
    return [Track(match) for match in matches]

