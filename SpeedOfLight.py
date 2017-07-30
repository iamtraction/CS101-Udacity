# Write Python code to print out how far light travels
# in centimeters in one nanosecond.

speed_of_light = 299792458   # meters per second
centimeters = 100            # one meter is 100 centimeters
nanosecond = 1.0/1000000000  # one billionth of a second

# Nanostick: A stick that's lenght is same as the length
# light travels in one nanosecond.
# Grace Hopper used to hold that.
nanostick = speed_of_light * centimeters * nanosecond

print nanostick
