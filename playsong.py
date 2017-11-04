import time
from pygame import mixer


playtimes = [1, 2, 3, 4, 5]

event_raw = []

with open ("show.txt", 'r') as show:
	event_raw = show.readlines()


next_frame = 0

mixer.init()
print("loading music")
mixer.music.load("./WizardsInWinter.mp3")

time.sleep(2)

mixer.music.play()

START_TIME = time.time()
RUN_TIME = 0.0

while True:
	PREV_TIME = RUN_TIME
	RUN_TIME = time.time() - START_TIME
	DELTA_TIME = RUN_TIME - PREV_TIME
	#print("DeltaTime: " + str(DELTA_TIME))
	
	frame = event_raw[next_frame]
	elements = frame.split(',')
	next_time = float(elements[0])
	
	event_string = ""
	
	for i in range(1, len(elements)):
		event_string = event_string + str(elements[i])
	
	if RUN_TIME >= next_time:
		print("Event: " + event_string)
		next_frame += 1
		if next_frame == len(event_raw):
			break

print("End")