# Marifel Villarroel 27650619
import fileinput
import os
def cls():
    os.system('cls')
class personas:

    def __init__(self, nombre, apellido, fecha_nacimiento, edad, pais_residencia, genero, estatus):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.pais_residencia = pais_residencia
        self.genero = genero
        self.estatus = estatus

    def registrar(self):
        registro = open('archivoPersonas.txt', 'a')

        registro.write(f'''
Nombre: {self.nombre}
Apellido: {self.apellido}
Fecha_nacimiento: {self.fecha_nacimiento}
Edad: {self.edad}
Pais: {self.pais_residencia}
Genero: {self.genero}
Estatus: {self.estatus}
-------------------------------------''')
        registro.close()

    def mostrar(self):
        print(f'''Persona registrada
Nombre:{nombre}
Apellido:{apellido}
Fecha de nacimiento:{fecha_nacimiento}
Edad: {edad}
Pais de residencia: {pais_residencia}
Genero: {genero}
Estatus: {estatus}
''')

salida = False

while salida == False:
    cls()
    print('\033[1:30m ')
    print('''Ingrese una opcion
    1- Registrar persona sospechosa
    2- Ver registros por: pais, genero, edad o casos
    3- Determinar si una persona tiene o no codvi-19
    4- Actualizar casos activos(recuperados y fallecidos)
    5- Ver personas registradas
    6- Eliminar todos los datos guardados 
    7- Salir del programa
    ''')


    opcion = input()
    if opcion == '1':
        # Registra a las personas como un estatus sospechoso
        print('Ingrese los datos de la persona con posible caso de coronavirus')
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        fecha_nacimiento = input('Fecha de nacimiento: ')
        pais_residencia = input('Pais de residencia: ')
        edad = input('Edad: ')
        estatus = 'Sospechoso'
        print('''Selecione el genero
        1- Femenino
        2- Masculino
        ''')

        opcion1 = input()
        if opcion1 == '1':
            genero = 'Femenino'
        elif opcion1 == '2':
            genero = 'Masculino'
        else:
            print('Opcion incorrecta')
            continue
        NuevaPersona = personas(nombre, apellido, fecha_nacimiento, edad, pais_residencia, genero, estatus)
        NuevaPersona.registrar()
        NuevaPersona.mostrar()


    elif opcion == '2':
        opcion1 = 0
        while opcion1 != '5':

            print('''Ingrese una opcion para ver los casos
            1- Ver por pais 
            2- Ver por genero 
            3- Ver por edad
            4- ver casos: sospechosos, confirmados, descartados, recuperados y fallecidos
            5- Volver atras
            ''')
            opcion1 = input()
            registro = open('archivoPersonas.txt', 'r')
            lineas = registro.readlines()
            registro.close()
            # para ver los casos sospechos, confirmados y descartados
            # por pais
            if opcion1 == '1':
                pais = input('Escriba el nombre del pais: ')
                conteo_pais = lineas.count('Pais: ' + pais + '\n')
                conteo_paisS = lineas.count(('Pais: '+pais+'\n') and ('Estatus: '+'Sospechoso'+'\n'))
                conteo_paisC = lineas.count(('Pais: '+pais+'\n') and ('Estatus: '+'CONFIRMADO'+'\n'))
                conteo_paisD = lineas.count(('Pais: '+pais+'\n') and ('Estatus: '+'DESCARTADO'+'\n'))
                conteo_paisR = lineas.count(('Pais: '+pais+'\n') and ('Estatus: '+'Recuperado'+'\n'))
                conteo_paisF = lineas.count(('Pais: '+pais+'\n') and ('Estatus: '+'Fallecido'+'\n'))
                print(f'''Casos registrados en {pais}: {conteo_pais}
        Sospechosos: {conteo_paisS}
        Confirmados: {conteo_paisC}
        Descartados: {conteo_paisD}
        Recuperados: {conteo_paisR}
        Fallecidos: {conteo_paisF}
                ''')
                continue
            # por genero
            elif opcion1 == '2':
                conteo = lineas.count('Genero: ' + 'Femenino' + '\n')
                conteo1 = lineas.count(('Genero: ' + 'Femenino'+'\n') and ('Estatus: ' + 'Sospechoso'+'\n'))
                conteoFconfirmado = lineas.count(('Genero: '+'Femenino'+'\n') and ('Estatus: '+'CONFIRMADO'+'\n'))
                conteoFdescartado = lineas.count(('Genero: '+'Femenino'+'\n') and ('Estatus: '+'DESCARTADO'+'\n'))
                conteoFrecuperado = lineas.count(('Genero: '+'Femenino'+'\n') and ('Estatus: ' + 'Recuperado'+'\n'))
                conteoFfallecidos = lineas.count(('Genero: '+'Femenino'+'\n') and ('Estatus: '+'Fallecido'+'\n'))
                print(f'''Casos en mujeres: {conteo}
        Sospechosos: {conteo1}
        Confirmados: {conteoFconfirmado}
        Descartados:  {conteoFdescartado}
        Recuperados: {conteoFrecuperado}
        Fallecidos: {conteoFfallecidos}
                ''')

                conteoH = lineas.count('Genero: ' + 'Masculino' + '\n')
                conteoHsospechoso = lineas.count(('Genero: '+'Masculino: '+'\n') and ('Estatus: '+'Sospechoso'+'\n'))
                conteoHconfirmados = lineas.count(('Genero: '+'Masculino'+'\n') and ('Estatus: '+'CONFIRMADO'+'\n'))
                conteoHdescartado = lineas.count(('Genero: '+'Masculino: '+'\n') and ('Estatus: '+'DESCARTADO'+ '\n'))
                conteoHrecuperados = lineas.count(('Genero: '+'Masculino'+'\n') and ('Estatus: '+'Recuperado'+'\n'))
                conteoHfallecidos = lineas.count(('Genero: '+'Masculino''\n') and ('Estatus '+ 'Fallecido'+'\n'))
                print(f'''Casos en hombres: {conteoH}
        Sospechosos: {conteoHsospechoso}
        Confirmados: {conteoHconfirmados}
        Descartados: {conteoHdescartado}
        Recuperados {conteoHrecuperados}
        Fallecidos: {conteoHfallecidos}
                ''')

                continue
            # por edad
            elif opcion1 == '3':
                persona_edad = input('Ingrese la edad: ')
                conteo_edad = lineas.count('Edad: ' + persona_edad + '\n')
                conteo_edadS = lineas.count(('Edad: '+ persona_edad+'\n') and ('Estatus: '+'Sospecho'+'\n'))
                conteo_edadC = lineas.count(('Edad: '+ persona_edad+'\n') and ('Estatus: '+'CONFIRMADO'+'\n'))
                conteo_edadD = lineas.count(('Edad: '+ persona_edad+'\n') and ('Estatus: '+'DESCARTADO'+'\n'))
                conteo_edadR = lineas.count(('Edad: '+ persona_edad+'\n') and ('Estatus: '+'Recuperado'+'\n'))
                conteo_edadF = lineas.count(('Edad: '+ persona_edad+'\n') and ('Estatus: '+'Fallecido'+'\n'))
                print(f'''Casos en personas con {persona_edad} años: {conteo_edad}
                Sospechosos: {conteo_edadS}
                Confirmados: {conteo_edadC}
                Descartados: {conteo_edadD}
                Recuperados: {conteo_edadR}
                Fallecidos: {conteo_edadF}
                ''')
                continue
            elif opcion1 == '4':
            # Para ver por casos
                conteo_sospechosos = lineas.count('Estatus: '+'Sospechoso'+'\n')
                conteo_confirmados = lineas.count('Estatus: '+'CONFIRMADO'+'\n')
                conteo_descartados = lineas.count('Estatus: '+'DESCARTADO'+'\n')
                conteo_recuperados = lineas.count('Estatus: '+'Recuperado'+'\n')
                conteo_fallecidos = lineas.count('Estatus: '+'Fallecido'+'\n')
                print(f'''CASOS
        Sospechosos: {conteo_sospechosos}
        Confirmados: {conteo_confirmados}
        Descartados: {conteo_descartados}
        Recuperados: {conteo_recuperados}
        Fallecidos: {conteo_fallecidos}
                ''')
                continue

            elif opcion1 == '5':
                break
            else:
                print('Opcion incorrecta')
    elif opcion == '3':
        # Para registrar a una persona como confirmado o descartado en un posible caso de codvi-19
        print('Ingrese los datos de la persona con posible caso de coronavirus')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        fecha_nacimiento = input('Fecha de nacimiento: ')
        pais_residencia = input('Pais de residencia: ')
        edad = input('Edad: ')
        print('''Selecione el genero
    1- Femenino
    2- Masculino
    ''')
        opcion1 = input()
        if opcion1 == '1':
            genero = 'Femenino'
            print('''Selecione los sintomas que posee la persona
    1- Fiebre, tos seca, dificultad para respirar, dolor de cabeza y muscular
    2- Tos con flema, moqueo frecuente, estornudos y malestar de garganta
    3- Estornudos, congestion y aguilla nasal
    ''')
            opcion2 = input()
            if opcion2 == '1':
                print('\033[1:36m ')
                print('DIAGNOSTICO: codvi-19 ')
                print('\033[0:00m ')
                estatus = 'CONFIRMADO'
            elif opcion2 == '2':
                print('\033[1:36m ')
                print('DIAGNOSTICO: resfriado comun')
                print('\033[0:00m ')
                estatus = 'DESCARTADO'
            elif opcion2 == '3':
                print('\033[1:36m ')
                print('DIAGNOSTICO: alergia')
                print('\033[0:00m ')
                estatus = 'DESCARTADO'
            else:
                print('-----------------OPCION INVALIDA')
        elif opcion1 == '2':
            genero = 'Masculino'
            print('''Selecione los sintomas que posee la persona
            1- Fiebre, tos seca, dificultad para respirar, dolor de cabeza y muscular
            2- Tos con flema, moqueo frecuente, estornudos y malestar de garganta
            3- Estornudos, congestion y aguilla nasal
            ''')
            opcion2 = input()
            if opcion2 == '1':
                print('\033[1:36m ')
                print('CASO DE CORONAVIRUS ')
                print('\033[0:00m ')
                estatus = 'CONFIRMADO'
            elif opcion2 == '2':
                print('\033[1:36m ')
                print('La persona tiene un resfriado comun')
                print('\033[0:00m ')
                estatus = 'DESCARTADO'
            elif opcion2 == '3':
                print('\033[1:36m ')
                print('La persona sufre de alergia')
                print('\033[0:00m ')
                estatus = 'DESCARTADO'
            else:
                print('------------------OPCION INVALIDA')
        else:
            print('-------------------OPCION INVALIDA')
            continue
        NuevaPersona = personas(nombre, apellido, fecha_nacimiento, edad, pais_residencia, genero, estatus)
        NuevaPersona.registrar()
        NuevaPersona.mostrar()

    elif opcion == '4':
        # Para registrar a una persona con un estatus de recuperado o fallecido del codvi-19
        print('Ingrese los datos de la persona que se ha recuperado o fallecido')
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        fecha_nacimiento = input('Fecha de nacimiento: ')
        pais_residencia = input('Pais de residencia: ')
        edad = input('Edad: ')
        print('''Selecione el genero
        1- Femenino
        2- Masculino
        ''')
        opcion1 = input()
        cFemeninoS = 0
        cMasculinoS = 0
        if opcion1 == '1':
            genero = 'Femenino'
            print('''Ingrese opcion
        1- Persona recuperada
        2- Persona fallecida
        ''')
            opcion3 = input()
            if opcion3 == '1':
                estatus ='Recuperado'
            elif opcion3 == '2':
                estatus = 'Fallecido'
            else:
                print('Opcion incorrecta')
                continue
        elif opcion1 == '2':
            genero = 'Masculino'
            print('''Ingrese una opcion 
            1- Persona recuperada
            2- Persona fallecida
            ''')
            opcion3 = input()
            if opcion3 == '1':
                estatus = 'Recuperado'
            elif opcion3 == '2':
                estatus = 'Fallecido'
            else:
                print('Opcion incorrecta')
                continue
        else:
            print('Opcion incorrecta')
            continue
        NuevaPersona = personas(nombre, apellido, fecha_nacimiento, edad, pais_residencia, genero, estatus)
        NuevaPersona.registrar()
        NuevaPersona.mostrar()
    elif opcion == '5':
        # mostrar todos los datos
        registro = open('archivoPersonas.txt', 'r')
        mensaje = registro.read()
        print(mensaje)
        registro.close()
        continue
    elif opcion == '6':
        # vaciar toda la pantalla
        registro = open('archivoPersonas.txt','r')
        lineas = registro.readlines()
        registro.close()
        registro = open('archivoPersonas.txt', 'w')
        for linea in lineas:
            if linea != ' ' + '\n':
                registro.write(linea)
        registro.close()

    if opcion == '7':
        print('Fin del programa, recuerde lavarse las manos')
        salida = True
    else:
        print('')
