def get_even_list(l):
        s=[]
        for i in range(len(l)):
                if(l[i]%2==0):
                        s.append(l[i])
        print(s)
        return s
