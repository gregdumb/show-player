import time
from pygame import mixer
import RPi.GPIO as GPIO

ON = GPIO.HIGH
OFF = GPIO.LOW

pins = [4, 17, 27, 22, 5, 6, 13, 26]

GPIO.setmode(GPIO.BCM)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, OFF)

#led = LED(4)

def execute_pinout(states):
    int_states = [int(numeric_string) for numeric_string in states]
    print(str(int_states))
    max_range = min(len(pins), len(states))
    for i in range(0, max_range):
        if int_states[i] == 0:
            GPIO.output(pins[i], OFF)
        else:
            GPIO.output(pins[i], ON)

def play_show(audio_path, show_path):
    # Open show file
    event_raw = []
    with open (show_path, 'r') as show:
        event_raw = [line.rstrip() for line in show]
    
    next_frame = 0
    
    # Play music
    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init()
    print("loading music")
    mixer.music.load(audio_path)
    
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
            execute_pinout(elements)
            next_frame += 1
            if next_frame == len(event_raw):
                break
    
    mixer.music.fadeout(1000)
    execute_pinout([1,1,1,1,1,1,1,1])