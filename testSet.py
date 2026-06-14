import os
import sys

print("Iniciando Test Set Automatizado")

print("Ejecutando Test Case 1: Abrir Navegador Google")
resultado1 = os.system("python3 testMain.py")

if resultado1 == 0:
    print("Test Case 1 Finalizado con exito")
elif resultado1 != 0:    
    print("Test Case 1 Fallido...")
    #sys.exit(1)


print("Ejecutando Test Case 2: Realizar Busqueda en Google") 
resultado2 = os.system("python3 buscarMain.py")

if resultado2 == 0:
    print("Test Case 2 Finalizado con exito")
elif resultado2 != 0:    
    print("Test Case 2 Fallido...")
    #sys.exit(1)                


print("Test Set Automatizado Finalizado con los siguientes resultados:")

if resultado1 == 0 and resultado2 == 0:
    print("Todos los Test Cases se ejecutaron correctamente") 
elif resultado1 != 0 or resultado2 != 0:
    print("Algunos Test Cases fallaron, revisar logs para mas detalles")

    sys.exit()
    
