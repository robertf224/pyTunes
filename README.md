pyTunes
=======

A python scripting interface for iTunes.

Installation
------------

Mac OSx only

#### From PyPi:

``` bash
pip install pyTunes
```

#### From Source:

``` bash
git clone git://github.com/robertf224/pyTunes.git && cd pyTunes
python setup.py install
```

Convenience Functions
---------------------

pyTunes contains several useful convenience functions.

``` python
import pyTunes as pytunes

pytunes.playtrack('Someday')

pytunes.playartist('The Strokes')

pytunes.playalbum('Room on Fire')
```

These functions are all case insensitive, and playtrack also filters out terms in parentheses and brackets.

``` python
# This will play "Runaway [feat. Pusha T]"
pytunes.playtrack('rUnAwAY')
```

These functions could easily be applied to create interesting hacks.  For example, they could be tied with an API like that provied by Twilio to create a jukebox application, or be combined with a speech-to-text engine to make a voice-controlled iTunes remote.

Control Functions
-----------------

These are all pretty self-explanatory.  These functions could be used with a library like [BreakfastSerial](https://github.com/theycallmeswift/BreakfastSerial) to create an Arduino-based iTunes remote.

``` python
pytunes.skip()
# Will only go to beginning of song depending on how far into the song we are, may go to previous song
pytunes.back()
# Will definitely go to the previous song
pytunes.prev()

# Toggle Play/Pause
pytunes.playpause()
pytunes.play()
pytunes.pause()

# Toggle Mute/Unmute
pytunes.muteunmute()
pytunes.mute()
pytunes.unmute()

pytunes.setvolume(100)
pytunes.getvolume()

# Move to 1 minute 40 seconds into current song
pytunes.setposition(100)
pytunes.getposition()
```

Track Functions
---------------

pyTunes also provides a Track wrapper class that internally handles some track-related things.  Track objects can be obtained through several functions of pyTunes.

``` python
# Gets current track
track = pytunes.playing()

# info now holds a reference to a dictionary containing some metadata about the track
info = track.getinfo()

# matches now holds a reference to an array containing Track objects that match the search term (by name, artist, album, etc.)
matches = pytunes.search('rain')

# We can play a 5 second preview of each match
import time
for track in matches:
	track.play()
	time.sleep(5)
```
