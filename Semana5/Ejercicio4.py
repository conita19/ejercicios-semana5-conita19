'''Registro de asistencia diaria
En una oficina se registra la asistencia hasta que el trabajador ingresa 0.
Solicita repetidamente:
1 si asistió
0 para terminar
Al final, muestra cuántos días asistió.'''
asistencia=0
dias=1
while(dias!=0):
    dias=int(input("Dime si hoy has asistido a clases. Pon 1 para asitencia y 0 para inasistencia):"))
    if dias==1:
        asistencia+=1
    elif dias!=0:
        asistencia*=0
print(asistencia)


