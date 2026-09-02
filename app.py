gastos = []

print("Sistema de Control de Gastos Personales")

while True:
    print("""
    +=====================================+
    |                MENÚ                 |
    +=====================================+
    |       1. Registrar gasto            |
    |       2. Visualizar gastos          |
    |       3. Calcular total de gastos   |
    |       4. Salir                      |
    +=====================================+
    """)

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        descripcion = input("Ingresa la descripción del gasto: ")
        cantidad = float(input("Ingresa la cantidad del gasto: "))

        gasto = {
            "descripcion": descripcion,
            "cantidad": cantidad
        }

        gastos.append(gasto)

        print("Gasto registrado correctamente.")
        input("\nPresiona ENTER para continuar")

    elif opcion == "2":
        print("\n--- GASTOS REGISTRADOS ---")

        if len(gastos) == 0:
            print("No hay gastos registrados.")
        else:
            for i, gasto in enumerate(gastos, start=1):
                print(f"{i}. {gasto['descripcion']} - ${gasto['cantidad']:.2f}")
        input("\nPresiona ENTER para continuar")

    elif opcion == "3":
        total = 0
    
        for gasto in gastos:
            total += gasto["cantidad"]

        print(f"\nTotal de gastos: ${total:.2f}")
        input("\nPresiona ENTER para continuar")
        
    elif opcion == "4":
        print("Saliendo de la aplicación...")
        break

    else:
        print("Opción no válida.")
