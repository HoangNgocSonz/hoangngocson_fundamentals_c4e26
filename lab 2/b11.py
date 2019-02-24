def is_inside(a,b):
    if((b[0]<=a[0])and(b[1]<=a[1])and(b[0]+b[2]>=a[0])and(b[1]+b[3]>=a[1])):
        print("yes")
    else:
        print("no")

#is_inside([10,20],[5,10,30,40])