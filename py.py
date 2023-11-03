#while  loops, for, forEach
from time import sleep

stop = input("Enter the stopping point")
start = input("Enter the starting point")

# print(type(start))
# x = 10
# y = "10"
if start.isnumeric() and stop.isnumeric():
    start = int(start)
    stop = int(stop)

    counter = start

    while counter <= stop:
        print(f"counting{counter}")
        sleep(3)
        counter += 1
else:
    print("Invalid values. Enter integers only")