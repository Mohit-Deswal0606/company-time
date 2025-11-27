
overtime=0
fullday=0
halfday=0
absent=0
shortday=0

try:
    for a in range(1,4):
        print('data of employee',a)
        for i in range(1,6):
            print("day",i,"data")
            a = float(input("entry time ="))
            b =float( input("exit time ="))
            if a<=9 and b>18 or a<9 and b>=18:
              print("over time")
              overtime+=1
            elif a==9 and b==18:
              print("full day")
              fullday+=1
            elif a<=9 and b==13 or a==13 and b>=18:
              print("half day")
              halfday+=1
            elif a>9 and b>=18 or a<=9 and 13<b<=18:
              print("short day")
              shortday+=1
            else:
              print("absent")
              absent+=1

    print('------------------------')
    print('summary of employee weekly data')
    print('------------------------')
    print(f"overtime={overtime}")
    print(f"fullday={fullday}")
    print(f"halfday={halfday}")
    print(f"absent={absent}")
    print(f"short day={shortday}")
    print('------------------------')
except ValueError:
   print('please enter a valid value')
except:
   print('error')
else:
   print('data collected')
finally:
   print('code completed')