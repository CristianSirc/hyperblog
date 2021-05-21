#Maximo comun divisor(MCD) y Minimo comun multiplo (MCM)
#Greatest common divisor(GCD) and Last common multiple(LCM)
#Algoritmo de Euclides

def mcd_mcm(a,b):

    if(a>=b):
        divisor=a
        dividendo=b
    else:
        divisor=b
        dividendo=a
    res=1
    MCD=0
    while(res!=0):
        res = divisor%dividendo
        if res==0:
            MCD=dividendo
        #print("Divisor:",divisor," Dividendo:",dividendo," Residuo:",res)
        divisor=dividendo
        dividendo=res
    MCM=(a*b)//MCD
    return MCD,MCM 

#1032,180
x=int(input("Ingrese el primer numero: "))
y=int(input("Ingrese el segundo numero: "))

mcd,mcm = mcd_mcm(x,y)
print("El máximo común divisor es: ",mcd)
print("El mínimio común multiplo es: ",mcm)
