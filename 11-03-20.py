#Datos de administrador:
#Correo: administrador@gmail.com
#Clave: administrador

class usuario:

    def __init__(self, nombre, apellido, correo, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave


    def registrar(self):
        print('Registrar un usuario')
        archivo = open('registro.txt', 'a')
        archivo.write(f'''
nombre: {self.nombre}
apellido: {self.apellido}
correo: {self.correo}
Clave: {self.clave}
''')
        archivo.close()


salida = False
clave_encontrada = False
while salida == False:
    print('''1- Iniciar Sesion
2- Registrar
3- Salir ''')
    opcion = input()
    if opcion == '1':
        clave_encontrada = False
        correo_admi = 'administrador@gmail.com'
        clave_admi = 'administrador'
        archivo = open('registro.txt','r')
        lineas = archivo.readlines()
        archivo.close()
        correo_ingresado = input('Ingrese su correo: ')
        if 'correo: '+correo_ingresado+'\n' in lineas:
            clave_ingresada = input('Ingrese su clave: ')
            if 'Clave: '+clave_ingresada+'\n' in lineas:
                clave_encontrada = True
                print('Iniciaste exitosamente!')
            else:
                print('CLave incorrecta')
        elif correo_ingresado == correo_admi:
            clave_ingresada = input('Ingrese su clave: ')
            if clave_ingresada == clave_admi:
                print('Los usuarios creados son: ')
                archivo = open('registro.txt', 'r')
                print(archivo.read())
                archivo.close()
            else:
                print('Clave incorrecta')
        else:
            print('Correo invalido')
        if clave_ingresada != clave_admi and clave_encontrada== True:
            salir = True
            while salir == True:
                print('''Elija la operacion aritmetica que desea realizar
                1- Suma
                2- Resta
                3- Multiplicacion 
                4- Division
                5- Salir''')
                operacion = input()

                if operacion == '1':
                    n1 = int(input('ingrese el primer numero: '))
                    n2 = int(input('ingrese el segundo numero: '))
                    suma = n1 + n2
                    print(f'El resultado de la suma: {suma}')
                    print('')
                    print('''Elija una opcion: 
1- Realizar otra operacion 
2- Volver al menu anterior 
3- Salir''')
                    seleccion = input()
                    if seleccion == '1':
                        salida = True
                    elif seleccion == '2':
                        salida = False
                    elif seleccion == '3':
                        break
                    else:
                        print('Opcion invalida')


                elif operacion == '2':
                    n1 = int(input('ingrese el primer numero: '))
                    n2 = int(input('ingrese el segundo numero: '))
                    resta = n1 - n2
                    print(f'El resultado de su resta es: {resta}')
                    print('')
                    print('''Elija una opcion: 
1- Realizar otra operacion 
2- Volver al menu anterior 
3- Salir''')
                    seleccion = input()
                    if seleccion == '1':
                        salida = True
                    elif seleccion == '2':
                        salida = False
                    elif seleccion == '3':
                        break
                    else:
                        print('Opcion invalida')

                elif operacion == '3':
                    n1 = int(input('ingrese el primer numero: '))
                    n2 = int(input('ingrese el segundo numero: '))
                    multiplicacion = n1 * n2
                    print(f'El resultado de su multiplicacion es: {multiplicacion}')
                    print('')
                    print('''Elija una opcion: 
1- Realizar otra operacion 
2- Volver al menu anterior 
3- Salir''')
                    seleccion = input()
                    if seleccion == '1':
                        salida = True
                    elif seleccion == '2':
                        salida = False
                    elif seleccion == '3':
                        break
                    else:
                        print('Opcion invalida')


                elif operacion == '4':
                    n1 = int(input('ingrese el primer numero: '))
                    n2 = int(input('ingrese el segundo numero: '))
                    division = n1 / n2
                    print(f'El resultado de su division es: {division}')
                    print('''Elija una opcion: 
1- Realizar otra operacion 
2- Volver al menu anterior 
3- Salir''')
                    seleccion = input()
                    if seleccion == '1':
                        salida = True
                    elif seleccion == '2':
                        salida = False
                    elif seleccion == '3':
                        break
                    else:
                        print('Opcion invalida')

                elif operacion == '5':
                    break

                else:
                    print('Opcion invalida')


    elif opcion == '2':
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        correo = input('correo: ')
        clave = input('Clave: ')
        NuevoUsuario = usuario(nombre, apellido, correo, clave)
        NuevoUsuario.registrar()

    elif opcion == '3':
        salida = True

    else:
            print('Opcion invalida')

