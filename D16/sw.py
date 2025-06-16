import time

st = int(input("Enter value to start the stopwatch: "))

for i in range(st, 0, -1):
    print(f"00:00:{i}", end="\r")
    time.sleep(1)

print("Time Up!!!")