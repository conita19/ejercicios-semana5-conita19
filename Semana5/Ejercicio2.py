'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''
x=float(input("Dime una temperatura y te dire a que clasificacion de temperatura corresponde:"))
if x<10:
    print(x,"Es una temperatura fria")
elif (10<=x<=25):
    print(x,"Es una temperatura templada")
else:
    print(x,"Es una temperatura calurosa") 






