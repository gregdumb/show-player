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