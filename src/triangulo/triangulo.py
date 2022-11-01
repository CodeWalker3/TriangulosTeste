
def triangulo(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return("é um triangulo")
    else:
        return("não é um triangulo")

a = triangulo(3,5,6)

print (a)