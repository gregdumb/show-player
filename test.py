import time
from pygame import mixer

print("At least I'm doing something")

mixer.pre_init(44100, -16, 2, 2048)
print("Did pre init")
mixer.init()
print("Did init")
mixer.music.load("./WizardsInWinter.mp3")

print("About to play")

mixer.music.play()

start = time.time()
current = 0

while True:
	current = time.time() - start
	if(current > 5):
		print("Finished")
		break;

print("All done")