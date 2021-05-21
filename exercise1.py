"""
#Exercise1
def ident(cadena):
    if(cadena[29]==','):
        cadena[29+1]+"\n"
    return cadena

cad = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
i=0
while(i<30):
    print(cad[i])
    i+=1


cad = ident(cad)
print(cad)"""

"""import datetime
now = datetime.datetime.now()
print(now)
"""

"""
#import numpy as np
radio = int(input("Ingrese el radio: "))
area = (3.1416)*(radio**2)
print(area)"""

"""values = input("Ingrese la secuencia: ")
lista = values.split(",")
tupla = tuple(lista)
print(lista)
print(tupla)"""

"""nombre = input("Ingrese el nombre del archivo: ")
nombre = nombre.split(".")
ext = nombre[-1]
print(ext)"""

"""
exam_st_date = (11, 12, 2014)
#date = exam_st_date.split(",")
month = exam_st_date[0]
day = exam_st_date[1]
year = exam_st_date[2]
print(month, "/", day, "/",year)
"""

"""
#Imprimir descripcion de funciones buit in
#print(map.__doc__)
"""

"""
#Imprimir calendario
import calendar
year = int(input("Ingrese el anio: "))


for i in range(12):
    print(calendar.month(year,i+1))
"""

"""
#Diferencia entre dos fechas en dias
from datetime import date
fecha1 = date(2014, 7, 2)
fecha2 = date(2014, 7, 11)
dif = fecha2-fecha1
print(dif)
"""

"""
def difference(number):
    if number >= 17:
        return((number-17)*2)
    else:
        return(17-number)

numero = int(input("Ingrese un numero: "))
print(difference(numero))
"""

"""
numero = int(input("Ingrese un numero: "))
if numero<=2000:
    if numero<=1000:
        if numero<=100:
            print("El numero está dentro de 100")
        else:
            print("El numero está fuera de 100")
    else:
        print("El numero está fuera de 1000")
else:
    print("El numero está fuera de 2000")        
"""

"""
def sum_three(a,b,c):
    suma = a+b+c
    if a==b==c:
        mult=suma*3
        return mult
    else:
        return suma

resultado = sum_three(5,2,3)
print(resultado)
"""

"""
#19
def new_string(word):
    if word[0]=='I' and word[1]=='s':
        return word
    else:
        return 'Is' + word

print(new_string("remedio"))
w = "remedio"
print(w[2:4])
"""

"""
#20
string1 = input("Ingrese el string: ")
n=3
print(string1*n)
"""


"""
#21
def parity(num):
    if num%2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
print(parity(num))
"""

"""
#22
lista = [2,4,5,7,4,4,8,4,5,1]
suma=0
for i in lista:
    if i==4:
        suma=suma+1
print(suma)
"""

"""
#23
def copies_two(string,n):
    ad=""
    if len(string)<=2:
        return string*n
    else:
        ad=string[:2]*n
        return ad+string

print(copies_two("Mariposa",3))
"""

"""
#24
def is_vowel(letter):
    vowels=['a','e','i','o','u']
    count=0
    for i in vowels:
        if i==letter:
            count=count+1
        else:
            count+=0
    if count != 0:
        return True
    else:
        return False

print(is_vowel('e'))
print(is_vowel('t'))
print(is_vowel('u'))
print(is_vowel('o'))


print("De otra manera: ")

def is_vowel2(letter):
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        print(letter, " is a vowel")
    else:
        print(letter, " is not a vowel")

is_vowel2('a')
is_vowel2('t')
is_vowel2('i')

# Hasta el punto 30 en w3School
"""

"""
#25
def contained(num):
    group=[1,4,7,3,5,7,'f',9]
    count=0
    for i in group:
        if i==num:
            count=count+1
        else:
            count=count+0
    if count!=0:        
        print(num, "is in the group")
    else:
        print(num, "is not in the group")    

contained(3)
contained('f')
contained(5)


def contained2(num):
    group=[1,4,7,3,5,7,'f',9]
    for i in group:
        if num==i:
            return True
    return False

print(contained2(3))
print(contained2('p'))
print(contained2(5))

"""

"""
#26
caracter = input("Enter the caracter for the hist: ")
data = [13,3,7,6,32,2,1,4,8,9,17,20,30]
for i in data:
    #print(data.index(i))
    print(data.index(i)+1, " |", caracter*i)
"""

"""
#27
def concatenate(data):
    i=0
    data_pro=""
    while i<len(data):
        letter = str(data[i])
        data_pro = data_pro+letter
        i+=1
    return data_pro

def concatenate2(data):
    data_pro=""
    for i in data:
        data_pro += str(i) 
    return data_pro

data1 = [13,3,7,6,32,2,1,4,8,9,17,20,30]
print(concatenate(data1))
print(concatenate2(data1))
"""

#28
"""
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

even_numbers = []
for i in numbers:
    if i == 237:
        print(i)
        break
    elif i%2==0:
        even_numbers.append(i)
        
print(even_numbers)    
"""

"""
#29
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1-color_list_2)
print(color_list_1.difference(color_list_2))
"""

"""
#31
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

"""

"""
for i in range(5,10,2): #Inicio, final, Saltos de 2 en 2
    print(i)
"""

"""
#Video9 
contador_int = 0
contador_ext = 0

while contador_ext<5:
    while contador_int<7:
        print(contador_ext,contador_int)
        contador_int+=1
    contador_int=0
    contador_ext+=1

"""


#Esta es una nueva linea agregada con el fin de visualizar otras ramas
#Se trata de simples comentarios en python

multiplicacion = lambda x,y: x*y
print(multiplicacion(2,4))

suma = lambda x,y: x+y


def exhaustive(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        #print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} con exhaustive es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta<=objetivo:
        #print(abs(respuesta**2 - objetivo), respuesta)
        respuesta+=paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} con aproximacion es {respuesta}')


def bisection(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto+bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto+bajo)/2

    print(f'La raiz cuadrada de {objetivo} con bisection es {respuesta}')

exhaustive(4)
aproximacion(4)
bisection(4)