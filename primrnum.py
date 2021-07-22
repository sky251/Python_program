
def prim(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True

num = int(input("Enter num:")) 
lis=[x for x in range(1,num)]
prim_lst = filter(prim,lis)
print("list of prim numbers is\n",prim_lst)