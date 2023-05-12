import time
L = input("Insert the time to countdown 'h:m:d' ")
L = L.split(":")
sec = int(L[2])
while sec >= 60:
    sec = int(input("Please input the seconds again "))
mins = int(L[1])
while mins >= 60:
    mins = int(input("Please input the minutes again "))
hours = int(L[0])
def timer( h , m , s ):
    while h >= 0:
        print(str("%.2d"%h) + " : " + str("%.2d"%m) + " : " + str("%.2d"%s))
        if s != 0:
            time.sleep(1)
            s = s-1
        elif m != 0:
            m = m -1
            s = 59
            time.sleep(1)
        elif h != 0:
            h = h - 1
            m = 59
            s = 59
            time.sleep(1)
        else:
            h = -1
            print("The time is up")
timer(hours , mins , sec)
