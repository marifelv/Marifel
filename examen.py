class bailar:
    def __init__(self):
        self.GeneroCancion = ''
        self.EstiloBaile= ''
        self.Pareja= ''
        self.Musica = ''
        self.Cancion = ''

# PARA SELECCIONAR SI DESEA BAILAR CON MUSICA O SIN MUSICA

    def Principal(self):
        print('')
        seleccion= input('''Desea bailar con musica?
1=> Si
2=> No
Opcion: 
''')

        if seleccion=='1':
            self.Musica = 'Con'
            self.GeneroCancion=input('Escriba el genero de la cancion: ')
            print('')
            self.Cancion = input('Escriba el nombre de la cancion: ')
            print('')


        elif seleccion=='2':
            self.Musica='Sin'
            self.GeneroCancion= '-NO IDENTIFICADO-'
            self.Cancion= '-NO IDENTIFICADA-'
            print('Vamos a bailar sin musica')
            print('')

        else:
            self.Musica='-NO IDENTIFICADA-'
            self.GeneroCancion='-NO IDENTIFICADO-'
            self.Cancion = '-NO IDENTIFICADA-'
            print('   OPCION INVALIDA')
            print('-SIN MUSICA POR DEFECTO-')
            print('')


#PARA ELEGIR EL ESTILO DE BAILE

    def baile(self):
        if self.GeneroCancion == '-NO IDENTIFICADO-':
            self.EstiloBaile = 'Libre'
        else:
            self.EstiloBaile=input('Ingrese el estilo de baile: ')
            print('')

#PARA ELEGIR SI TIENE PAREJA DE BAILE O NO
    def pareja(self):
         seleccion =input('''Desea bailar con pareja?
1=si
2=no
Opcion: 
''')
         if seleccion=='1':
             self.Pareja='en pareja '

         elif seleccion=='2':
             self.Pareja= 'individual '

         else:
             self.Pareja='-SIN PAREJA POR DEFECTO-'
             print('OPCION INVALIDA')
             print('')

 # PARA MOSTRAR

    def bailando(self):
        print('VAMOS A BAILAR!')
        print('')
        print(f'{self.Musica} musica ')
        print(f'Cancion: {self.Cancion}')
        print(f'Genero de la cancion: {self.GeneroCancion}')
        print(f'Estilo de baile: {self.EstiloBaile}')
        print(F'Baile {self.Pareja}')

# MENU PRINCIPAL

seleccion=input('''Quieres bailar? 
Escribe el numero para elegir
1=>si
2=>no
Opcion: ''')

if seleccion=='1':
        seleccion = False
        while seleccion == False:
            bailarin = bailar()
            bailarin.Principal()
            bailarin.baile()
            bailarin.pareja()
            bailarin.bailando()

            seleccion=input('''Quieres bailar otra vez
                1= si
                2= no
                Opcion: ''')
            if seleccion =='1':
                seleccion=False
            elif seleccion=='2':
                print('Seguiremos bailando en otra ocacion...')
                seleccion=True
            else:
                print('OPCION INVALIDA')

elif seleccion=='2':
        print('Bailaremos en otra ocacion...')

else:
        print('OPCION INVALIDA')



























