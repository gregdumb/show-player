import time
import sys
from pygame import mixer
import gpio_player as gpio

if(len(sys.argv) < 3):
	sys.exit()

SONG_PATH = sys.argv[1]
SHOW_PATH = sys.argv[2]

print(sys.argv[1])

event_raw = []

with open (SHOW_PATH, 'r') as show:
    event_raw = [line.rstrip() for line in show]

next_frame = 0

# Play music
mixer.pre_init(44100, -16, 2, 2048)
mixer.init()
print("loading music")
mixer.music.load(SONG_PATH)

mixer.music.play()

START_TIME = time.time()
RUN_TIME = 0.0

while True:
	PREV_TIME = RUN_TIME
	RUN_TIME = time.time() - START_TIME
	DELTA_TIME = RUN_TIME - PREV_TIME
	
	frame = event_raw[next_frame]
	elements = frame.split(',')
	next_time = float(elements[0])
	
	event_string = ""
	
	for i in range(1, len(elements)):
		event_string = event_string + str(elements[i])
	
	if RUN_TIME >= next_time:
		elements.pop(0)
		gpio.execute_pinout(elements)
		next_frame += 1
		if next_frame == len(event_raw):
			break

print("End")
