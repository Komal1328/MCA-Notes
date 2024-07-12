import pyfirmata2
import time

# Initialize the Arduino board on COM4
board = pyfirmata2.Arduino('COM4')

# Define the pins for the traffic signals for four lanes within the available range
pins = {
    'signal1': {'red': 13, 'yellow': 12, 'green': 11},
    'signal2': {'red': 10, 'yellow': 9, 'green': 8},
    'signal3': {'red': 7, 'yellow': 6, 'green': 5},
    'signal4': {'red': 4, 'yellow': 3, 'green': 2}
}

# Delays in seconds
red_delay = 10  # 10 seconds
yellow_delay = 2  # 2 seconds
green_delay = 8  # 8 seconds
inter_green_delay = 3  # Inter-green delay between signals in seconds

# Function to set the light state (HIGH or LOW) for a specific signal and color
def set_light(signal, color, state):
    pin = pins[signal][color]
    board.digital[pin].write(state)
    print(f"Set {signal} {color} to {state}")

# Function to turn off the green light for a specific signal
def turn_off_green(signal):
    set_light(signal, 'green', 0)
    time.sleep(0.1)

# Function to handle a traffic light cycle for a specific signal
def traffic_light_cycle(signal):
    print(f"{signal} cycle started")

    # Set all other signals' red lights
    for key in pins:
        if key != signal:
            set_light(key, 'red', 1)

    # Turn on the green light
    set_light(signal, 'red', 0)
    set_light(signal, 'yellow', 0)
    set_light(signal, 'green', 1)
    time.sleep(green_delay)

    # Turn on the yellow light
    set_light(signal, 'green', 0)
    set_light(signal, 'yellow', 1)
    time.sleep(yellow_delay)

    # Turn on the red light
    set_light(signal, 'yellow', 0)
    set_light(signal, 'red', 1)
    time.sleep(inter_green_delay)


    # Turn off the green light
    # turn_off_green(signal)

# Main loop to run the traffic light cycles for all four signals
while True:
    try:
        traffic_light_cycle('signal1')
        traffic_light_cycle('signal2')
        traffic_light_cycle('signal3')
        traffic_light_cycle('signal4')
    except KeyboardInterrupt:
        print("Traffic light cycle stopped by user.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break
