gastos = []

print("Sistema de Control de Gastos Personales")

descripcion = input("Ingresa la descripción del gasto: ")
cantidad = float(input("Ingresa la cantidad del gasto: "))

gasto = {
    "descripcion": descripcion,
    "cantidad": cantidad
}

gastos.append(gasto)

print("Gasto registrado correctamente.")
print(f"Gasto: {descripcion} - ${cantidad:.2f}")
