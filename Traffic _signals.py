import time

def countdown_timer(duration):
    """Display a countdown timer from the given duration (in seconds)."""
    for seconds in range(duration, 0, -1):
        print(f"Time remaining: {seconds} seconds", end="\r")
        time.sleep(1)
    print(" " * 30, end="\r")  # Clear the line after countdown finishes.

def traffic_signal():
    while True:
        # North Road Green
        print("North road: Green light")
        print("South road: Red light")
        print("West road: Red light")
        print("Pedestrian crossing: Red light")
        countdown_timer(60)

        # South Road Green
        print("\nSouth road: Green light")
        print("North road: Red light")
        print("West road: Red light")
        print("Pedestrian crossing: Red light")
        countdown_timer(60)

        # West Road Green
        print("\nWest road: Green light")
        print("North road: Red light")
        print("South road: Red light")
        print("Pedestrian crossing: Red light")
        countdown_timer(60)

        # Pedestrian Crossing
        print("\nPedestrian crossing: Green light")
        print("North road: Red light")
        print("South road: Red light")
        print("West road: Red light")
        countdown_timer(30)

        # Indicate free left and U-turn
        print("\nNote: Free left and U-turn are available for all roads.\n")

# Run the traffic signal system
traffic_signal()
