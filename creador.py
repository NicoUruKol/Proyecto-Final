from colorama import Back, Fore, Style, init
init(autoreset=True)

import json

color_error = Fore.RED
color_ok = Fore.GREEN+Style.BRIGHT
color_fondo = Fore.BLACK+Back.YELLOW+Style.BRIGHT
color_subtitulo = Fore.CYAN+Style.BRIGHT
color_menu = Fore.LIGHTCYAN_EX
color_submenu = Fore.BLUE
color_totales = Fore.CYAN

try:
    archivo = open("productos.json", "r")
    lista_producto = json.load(archivo)
    archivo.close()
except:
    lista_producto=[]

def limpiar_terminal():
    print("\033[H\033[J")

def diseño_titulo(titulo, ancho=66): 
    
    titulo_centrado = titulo.center(ancho)
    print("=" * ancho)
    print(Fore.CYAN+Style.BRIGHT+Back.WHITE+titulo_centrado.upper())
    print("=" * ancho)

def diseño_subtitulos(sub_titulo, ancho=66):
    subtitulo_centrado = sub_titulo.center(ancho)
    print("-" * ancho)
    print(Fore.CYAN+subtitulo_centrado.title())
    print("-" * ancho)

def separador(ancho=66):
    print("-" * ancho)

def cierre_cuadro_sup():
    print(color_subtitulo+"╔",end="")
    print(color_subtitulo+"═"*64, end="")
    print(color_subtitulo+"╗")

def cierre_cuadro_inf():
    print(color_subtitulo+"╚",end="")
    print(color_subtitulo+"═"*64, end="")
    print(color_subtitulo+"╝")

def cierre_cuadro_izq():
    print(color_subtitulo+"║", end="")

def cierre_cuadro_der():
    print(color_subtitulo + "║")

def primer_menu():
    diseño_titulo("Menu Manejo de stock")
    print()
    print(color_menu + "1. Articulos (Crea/Modifica/Elimina)")
    print(color_menu + "2. Movimientos (Ingreso/Egreso)")
    print(color_menu + "3. Informes (Listar/Buscar/Historial/Filtrar)")
    print()
    separador()
    print("0. Cerrar el programa")
    print()


def validar_codigo(cod):
    resultado = False
    for articulo in lista_producto:
        if articulo["codigo"] == cod:
            resultado = True
    return resultado

def crear(lista_producto):
    separador()
    print(color_subtitulo+Style.BRIGHT+"Creación de artículos")
    separador()
    while True:
        try:
            print("Ingrese un nuevo código de 6 dígitos")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = input("Su nuevo código: ").strip()
            if codigo == "0":
                return lista_producto
            
            codigo = int(codigo)
            if len(str(codigo)) != 6:
                print()
                print(color_error + "El código debe tener exactamente 6 dígitos. Intente nuevamente.")
                separador()
                continue
            elif validar_codigo(codigo):
                print()
                print(color_error + "Código repetido, intente nuevamente.")
                separador()
                continue
            else:
                False

            separador()
            print("Ingrese los datos de su articulo")
            print()
            bodega =     input("Bodega........: ").title()
            cepa   =     input("Cepa..........: ").title()
            linea  =     input("Linea.........: ").title()
            pais   =     input("Pais.........: ").title()
            region =     input("Region........: ").title()
            
            bucle_anio = True
            while bucle_anio:
                try:
                    anio   = int(input("Año...........: "))
                    bucle_anio = False
                except ValueError:
                    print()
                    print(color_error + "Entrada inválida. Por favor, ingrese un número entero.")
                    separador()

            bucle_precio = True
            while bucle_precio:
                try:
                    precio = float(input("Precio........: $"))
                    bucle_precio = False
                except ValueError:
                    print()
                    print(color_error + "Entrada inválida. Por favor, ingrese un valor.")
                    separador()

            print()
            print(color_ok+"El artículo ha sido CREADO con éxito!")
            print()

            vino = {
                "codigo": codigo,
                "bodega": bodega,
                "cepa": cepa,
                "pais": pais,
                "region": region,
                "linea": linea,
                "anio": anio,
                "precio": precio,
                "historial": []}
            
            lista_producto.append(vino)

            archivo = open("productos.json", "w")
            json.dump(lista_producto, archivo)
            archivo.close()

            return lista_producto
    
        except ValueError:
                print()
                print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
                separador()

def modificar(lista_producto):
    separador()
    print(color_subtitulo+Style.BRIGHT+"Modificación de artículos")
    separador()
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = input("Su código: ")
            
            if codigo == "0":
                print("Volviendo al menú anterior.")
                return lista_producto
            
            codigo = int(codigo)
            
            
            aux = validar_codigo(codigo)
            if aux == False:
                print()
                print(color_error+"Codigo inexistente, intente nuevamente")
                separador()
            else:
                for vino in lista_producto:
                    if codigo == vino["codigo"]:
                        print()
                        print(f"Bodega......:", vino['bodega'])
                        print(f"Cepa........:", vino['cepa'])
                        print(f"Linea.......:", vino['linea'])
                        print(f"País......:", vino['pais'])
                        print(f"Region......:", vino['region'])
                        print(f"Año.........: {vino['anio']}")
                        print(f"Precio......: $ {vino['precio']:.2f}")
                        separador()
                        print()
                        bodega_viejo =    vino['bodega']
                        cepa_viejo   =    vino['cepa']
                        linea_viejo  =    vino['linea']
                        pais_viejo =    vino['pais']
                        region_viejo =    vino['region']
                        anio_viejo   =    vino['anio']
                        precio_viejo =    vino['precio']
                        movimiento   =    vino['historial']

                        print(color_totales+"Dejar en blanco para mantener el dato anterior")
                        separador()
                        bodega =     input("Bodega........: ").title()
                        cepa   =     input("Cepa..........: ").title()
                        linea  =     input("Linea.........: ").title()
                        pais =     input("País........: ").title()
                        region =     input("Region........: ").title()
                        
                        while True:
                            anio = input("Año...........: ")
                            if anio == "":
                                anio = anio_viejo
                                break
                            try:
                                anio = int(anio)
                                break
                            except ValueError:
                                print(color_error + "Por favor, ingrese un año válido.")

                        while True:
                            precio = input("Precio........: $ ")
                            if precio == "":
                                precio = precio_viejo
                                break
                            try:
                                precio = float(precio)
                                break
                            except ValueError:
                                print(color_error + "Por favor, ingrese un precio válido.")

                        separador()
                        
                        if len(bodega) == 0:
                            bodega_nuevo = bodega_viejo
                        else:
                            bodega_nuevo = bodega
                        
                        if len(cepa) == 0:
                            cepa_nuevo = cepa_viejo
                        else:
                            cepa_nuevo = cepa

                        if len(linea) == 0:
                            linea_nuevo = linea_viejo
                        else:
                            linea_nuevo = linea

                        if len(pais) == 0:
                            pais_nuevo = pais_viejo
                        else:
                            pais_nuevo = pais

                        if len(region) == 0:
                            region_nuevo = region_viejo
                        else:
                            region_nuevo = region

                        for indice, vino in enumerate(lista_producto): 
                            if codigo == vino['codigo']:
                                del lista_producto[indice]
                        
                        vino = {
                            "codigo": codigo,
                            "bodega": bodega_nuevo,
                            "cepa": cepa_nuevo,
                            "linea": linea_nuevo,
                            "pais": pais_nuevo,
                            "region": region_nuevo,
                            "anio": anio,
                            "precio": precio}
                                        
                        lista_producto.append(vino)

                        archivo = open("productos.json", "w")
                        json.dump(lista_producto, archivo)
                        archivo.close()

                        print()
                        print(color_ok+"El articulo ha sido MODIFICADO con exito!")
                        print()
                        cierre_cuadro_sup()
                        cierre_cuadro_izq()
                        print(f" Bodega.....: {vino['bodega'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Cepa.......: {vino['cepa'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Linea......: {vino['linea'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" País.......: {vino['pais']:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Region.....: {vino['region'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Año........: {vino['anio']:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Precio.....: $ {vino['precio']:<47.2f} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_inf()
                        return lista_producto 
                break
        except ValueError:
                print()
                print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
                separador()

def eliminar(lista_producto):
    separador()
    print(color_subtitulo + Style.BRIGHT + "Eliminación de artículos")
    separador()
    
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = input("Su código: ")
            
            if codigo == "0":
                print("Volviendo al menú anterior.")
                return lista_producto
            
            codigo = int(codigo)
            
            articulo_encontrado = False
            for vino in lista_producto:
                if vino["codigo"] == codigo:
                    articulo_encontrado = True
                    
                    print()
                    print(f"Bodega.......: {vino['bodega']}")
                    print(f"Cepa.........: {vino['cepa']}")
                    print(f"Linea........: {vino['linea']}")
                    print(f"País.......: {vino['pais']}")
                    print(f"Región.......: {vino['region']}")
                    print(f"Año..........: {vino['anio']}")
                    print(f"Precio.......: {vino['precio']:.2f}")
                    print()
                    
                    confirmacion = input("¿Está seguro que desea eliminar este artículo? (SI/NO): ").strip().lower()
                    
                    while confirmacion not in ["si", "no"]:
                        print()
                        print(color_error + "Por favor, responda con 'SI' o 'NO'.")
                        confirmacion = input("¿Está seguro que desea eliminar este artículo? (SI/NO): ").strip().lower()
                    
                    if confirmacion == "si":
                        lista_producto.remove(vino)
                        
                        archivo = open("productos.json", "w")
                        json.dump(lista_producto, archivo)
                        archivo.close()
                        
                        print()
                        print(color_ok + "El artículo ha sido ELIMINADO con éxito!")
                        separador()
                        return lista_producto
                    else:
                        print()
                        print(color_error+"Operación cancelada. Volviendo al menú anterior.")
                        separador()
                        return lista_producto
            
            if not articulo_encontrado:
                print()
                print(color_error + "Código inexistente, intente nuevamente.")
                separador()
        
        except ValueError:
            print()
            print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
            separador()

def menu_carga(lista_producto):
    while True:
        print()
        print()
        separador()
        print(color_submenu+Style.BRIGHT+"Sub-menu de articulos")
        separador()
        print(color_submenu+"1. Crear articulos")
        print(color_submenu+"2. Modificar articulos")
        print(color_submenu+"3. Eliminar articulos")
        print()
        separador()
        print("0. Volver al menu anterior")
        print()
        opcion = input("Ingrese su opción: ")
        separador()

        match opcion:
            case "1":
                limpiar_terminal()
                lista_producto = crear(lista_producto)
            case "2":
                limpiar_terminal()
                lista_producto = modificar(lista_producto)
            case "3":
                limpiar_terminal()
                lista_producto = eliminar(lista_producto)
            case "0":
                primer_menu()
                break
            case _:
                print()
                print(color_error+"Opción no válida. Intente de nuevo.")
                separador()



diseño_titulo("TANNAT & CO.")
diseño_subtitulos("Bienvenido a la interfaz de Stock")
menu_carga(lista_producto)