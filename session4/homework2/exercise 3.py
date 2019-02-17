print ("if x =8, then what is the value of 4(x+3) ?")
print("1. 11")
print("2. 22")
print("3. 33")
print("4. 44")
count=0
a=int(input("your choice ? "))
if a==4:
    print("Bingo")
    count+=1
else:
    print(":(")

print ("1+1= ?")
print("1. 10")
print("2. 2")
print("3. 30")
print("4. 40")
a=int(input("your choice ? "))

if a==2:
    print("Bingo")
    count +=1
else:
    print(":(")

print ("you correctly answer",count,"out of 2 questions")