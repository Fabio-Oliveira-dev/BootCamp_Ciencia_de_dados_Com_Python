# Classe e inializador. 
#O self é uma referencia para o objeto. Atributos da classe

class bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        
#Definir metodos. Eu uso o def para definir o metodo e defino o argumento self
    def buzinar(self):
        print('Bi Bi...')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada')

    
    def correr(self):
        print('Vruuum...')

    def trocar_marcha(nro_marcha):
        print('Marcha trocada...')

    # Outro meio de exebição para o usuario
    #def __str__(self):
        #return f'Bicicleta: Cor={self.cor}, Modelo={self.modelo}, Ano={self.ano}, Valor={self.valor}'
        
    # Um pouco mais automatizado pegando o atributo (name) da classe
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Instanciar a bicicleta
#b1 = bicicleta('vermelha', 'monark', 2010, 1000)
#b1.buzinar()
#b1.correr()
#b1.parar()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta('Amarela', 'Caloi', 2022, 800)
print(b2)
b2.trocar_marcha()
