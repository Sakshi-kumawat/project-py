import time
import sys

def digital_clock():
    """Displays a digital clock."""
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        sys.stdout.write("\rDigital Clock: " + current_time)
        sys.stdout.flush()
        time.sleep(1)
    
# Solution as follows
def countdown_timer(seconds):
    """Counts down from a given number of seconds."""
    print("Countdown Timer started!")
    while seconds > 0:
        sys.stdout.write("\rTime remaining: " + str(seconds) + " seconds")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")


while (1):
    choice = input("Choose an option (1: Digital Clock, 2: Countdown Timer): ")

    if choice == "1":
        digital_clock()
    elif choice == "2":
        seconds = int(input("Enter the number of seconds to countdown: "))
        countdown_timer(seconds)
    else:
        print("Invalid choice!")