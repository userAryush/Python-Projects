import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
time.sleep(2)
if(12>int(time.strftime('%H'))>0):
    print("Goodmoring")
elif(12<int(time.strftime('%H'))<6):
    print("Goodafternoon")
else:
    print("GoodEvening")