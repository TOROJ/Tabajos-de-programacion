def promedio_R(A):
    s=0
    for i in ((A)):
        s+=i
    if (len(A)<=0):
        return "es vacio"
    else:
        s/=len(A)
        return s

def main():

    a=[1,2,4]
    print(promedio_R(a))
if __name__=="__main__":
    main()
