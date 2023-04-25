# Import the math module so I can math.pi
# Import the datetime class from the datetime
# # module so that it can be used in this program.
import math
from datetime import datetime

def main():
     # Print a description of this program for the user to see.

     print("The volume of a tire.")

     # Get the width , aspect ratio and diameter from the user.
     width = int(input("Enter the width of the tire in mm (ex 205): "))
     aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
     diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
     # Compute the volume of the tire.
     volume = (math.pi * (width * width) * aspect_ratio * ((width * aspect_ratio ) + (2540 * diameter))) / 10000000000

     print(f"The approximate volume is {round(volume, 2)} liters")

     # Call the now() method to get the current
     # date and time as a datetime object from
     # the computer's operating system.
     current_date_and_time = datetime.now()
     # Test

     # Save to file
     with open("volumes.txt", "a") as tire_volume_file:
          tire_volume_file.write(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {round(volume, 2)}\n")

main()

