import time
import random
import gpio_player as gpio

num_channels = 8



while True:
	
	state = [random.randint(0, 1) for _ in xrange(8)]
	
	gpio.execute_pinout(state)
	
	time.sleep(0.25)
	
	
