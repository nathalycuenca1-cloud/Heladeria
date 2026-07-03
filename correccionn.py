def mostrar_bienvenida():
    print("==============================================")
    print("            *** ICE ONLY HERE ***             ")
    print("     La heladeria mas fria de la ciudad!      ")
    print("==============================================")
    print("Como te llamas?")
    nombre = input()
    print("Hola", nombre, " Que gusto tenerte aqui:)")
    print("")
    print("Deseas hacer un pedido?")
    print(" 1. Si")
    print(" 2. No")
    opcion = int(input())
    return nombre, opcion

def menu(total_acumulado):
    print("=============================================")
    print("               MENU ICE ONLY HERE            ")
    print("=============================================")
    print(" Helados ")
    print("  1. Cono simple           $1.50")
    print("  2. Cono doble            $2.50")
    print("  3. Sundae clasico        $3.00")
    print(" Malteadas")
    print("  4. Malteada de fresa     $3.50")
    print("  5. Malteada chocolate    $4.00")
    print("  6. Malteada tropical     $4.50")
    print(" Postres Frios ")
    print("  7. Brownie con helado    $4.00")
    print("  8. Waffle frio           $5.00")
    print("  9. Copa mixta especial   $6.00")
    print("=============================================")
    print(" Total acumulado: $", total_acumulado)
    print("=============================================")

def dar_producto(opcion):
    orden = ""
    precio_unitario = 0.0

    if opcion == 1:
        precio_unitario = 1.50
        orden = "Cono simple"
    elif opcion == 2:
        precio_unitario = 2.50
        orden = "Cono doble"
    elif opcion == 3:
        precio_unitario = 3.00
        orden = "Sundae clasico"
    elif opcion == 4:
        precio_unitario = 3.50
        orden = "Malteada de fresa"
    elif opcion == 5:
        precio_unitario = 4.00
        orden = "Malteada chocolate"
    elif opcion == 6:
        precio_unitario = 4.50
        orden = "Malteada tropical"
    elif opcion == 7:
        precio_unitario = 4.00
        orden = "Brownie con helado"
    elif opcion == 8:
        precio_unitario = 5.00
        orden = "Waffle frio"
    elif opcion == 9:
        precio_unitario = 6.00
        orden = "Copa mixta especial"
    else:
        precio_unitario = 0.0
        orden = "Producto Desconocido"

    return orden, precio_unitario

def procesar_pedido(nombre, total_actual):
    print(nombre, ", que deseas ordenar? (1-9):")
    opcion = int(input())
    print("Cuantas unidades deseas?")
    cantidad = int(input())
    
    orden, precio_unitario = dar_producto(opcion)
    subtotal = precio_unitario * cantidad
    
    print("")
    print("Confirmas tu pedido?")
    print(" 1. Confirmar")
    print(" 2. Cancelar")
    confirmar = int(input())
    
    if confirmar == 1:
        total_actual = total_actual + subtotal
        print("=============================================")
        print(" Producto : ", orden)
        print(" Cantidad : ", cantidad)
        print(" Subtotal : $", subtotal)
        print(" Acumulado: $", total_actual)
        print("=============================================")
    else:
        print("Pedido cancelado, no hay problema ", nombre)
        
    return total_actual

def mostrar_factura_final(nombre, total):
    print("")
    print("==============================================")
    print(" FACTURA FINAL")
    print("==============================================")
    print(" Cliente: ", nombre)
    print(" Total a pagar: $", total)
    print(" Gracias por visitarnos, ", nombre)
    print(" Regresaaa pronto, te esperamos!")
    print("==============================================")

total = 0.0
nombre, opcion_inicio = mostrar_bienvenida()

if opcion_inicio == 1:
    continuar = 1
    while continuar == 1:
        menu(total)
    
        total = procesar_pedido(nombre, total)
        
        print("")
        print("Deseas agregar algo mas?")
        print(" 1. Si")
        print(" 2. No, solo quiero la factura final")
        continuar = int(input())
        
    mostrar_factura_final(nombre, total)
else:
    print("ok ", nombre, ", que tengas un lindo dia!")