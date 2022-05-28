import sys 

kg = float(sys.argv[1])
mts = float(sys.argv[2])/100

imc = kg / mts**2

#print(f"{imc:.2f}")

if imc < 18.5:
    print(f"Su IMC es {imc:.2f}\nLa clasificacion de la OMS es Bajo Peso")
elif imc < 25:
    print(f"Su IMC es {imc:.2f}\nLa clasificacion de la OMS Adecuado")
elif imc < 30:
    print(f"Su IMC es {imc:.2f}\nLa clasificacion de la OMS Sobrepeso")  
elif imc < 35:
    print(f"Su IMC es {imc:.2f}\nLa clasificacion de la OMS Obesidad Grado I")
elif imc < 40:
    print(f"Su IMC es {imc:.2f}\nLa clasificacion de la OMS Obesidad Grado II")
else:
    print(f"Su IMC es {imc:.2f}\nLa clasificacion de la OMS Obesidad Grado III")