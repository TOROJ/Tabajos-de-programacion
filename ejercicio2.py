def producto_p(A):
    a=0
    for i in (A):
        b=a
        a=i*i
        a=b+a
    return a


def main():

    s=[1,2,3]
    print(producto_p(s))
if __name__=="__main__":
    main()

    
    
