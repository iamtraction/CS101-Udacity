# Write Python code to print out how far light travels
# in one processor cycle.

speed_of_light = 299792458   # meters per second
cycles_per_second = 2.7 * 1000000000 # 2.7 GHz

traveled_distance = speed_of_light / cycles_per_second # meters

print traveled_distance * 100 # centimeters
