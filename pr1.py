def dict_cnt(str):
    w=str.split()
    count=dict()
    for a in w:
        if a in count:
            count[a]+=1
        else:
            count[a]=1
    return count
str="we are are here here we in "
c=dict_cnt(str)
print(c)
        
