print("Determinar si un año es el primer año de un siglo")
print("=================================================")

año = int(input("Introduce un año: "))

if año % 100 == 0:
    print(f"El año {año} es el primer año de un siglo.")
else:
    print(f"El año {año} no es el primer año de un siglo.")
