import sys
import os
import time
import glob
import ntpath
import gpio_player

if(len(sys.argv) < 3):
   sys.exit()

SONG_FOLDER = sys.argv[1]
SHOW_FOLDER = sys.argv[2]

LOOPING = False

if(len(sys.argv) > 3):
    if(sys.argv[3] == "1"):
        LOOPING = True

print("LOOPING: " + str(LOOPING))

show_query = SHOW_FOLDER + "*.txt"

show_list = (glob.glob(show_query))

while True:
    for showpath in show_list:
        # Get show filename and id
        showfile = ntpath.basename(showpath)
        showid = os.path.splitext(showfile)[0]
        
        songpath = glob.glob(SONG_FOLDER + showid + ".*")[0]
        
        gpio_player.play_show(songpath, showpath)
        
        time.sleep(3)
    
    if(LOOPING != True):
        break

