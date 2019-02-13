string = input ()
a = sorted(string.lower())
me= {}
for i in range(len(a)):
    if a[i].isalpha:
        me[a[i]] = a.count(a[i]) 
for i in me:
    print(i,  me[i])

