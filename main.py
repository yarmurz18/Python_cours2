import sys
import time

number_of_seconds = int(sys.argv[1])

for second in range(number_of_seconds):
    print(second)
    time.sleep(1)
