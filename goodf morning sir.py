import time
timestamp = time.strftime('%H:%M:%S')
H=int(timestamp[:2])
if(H<=12):
    print("good morning sir")
elif(H>=12):
    print("good evning sir")

print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
