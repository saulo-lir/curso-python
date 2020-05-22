# Por padrão, o Python não possui implementação para classes abstratas. Para isso, utilizamos a biblioteca ABC (Abstract Base Class). Com ela, conseguimos implementar métodos e classes abstratas em nossos programas.
import abc

# Definindo uma classe
class Veiculo(abc.ABC): # Informando o 'abc.ABC', estamos dizendo que a classe é abstrata
    # Construtor da classe. O python requer que passemos o valor 'self' em todo método que for criado
    def __init__(self, cor, tipo_combustivel, potencia):
        # Atributos da classe
        self._cor = cor # O '_' define o atributo como protected
        self.__tipo_combustivel = tipo_combustivel # O '__' define o atributo como privado
        self.__potencia = potencia
        self._qtd_combustivel = 0  # Valor default.
        self.__is_ligado = False    # Valor default
        self.__velocidade = 0   # Valor default

    # Destrutor da classe. Ele será chamado no final do script, destruindo o objeto que instanciou a classe e não está mais utilizando-a. Serve para desocupar a memória do servidor.
    def __del__(self):
        print('O objeto foi removido da memória.')

    def abastecer(self, qtd_combustivel):
        self.__qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            print('O veículo já está ligado!')
        else:
            self.__is_ligado = True
            print('O veículo foi ligado!')

    def desligar(self):
        if self.__is_ligado == False:
            print('O veículo já está desligado!')
        else:
            self.__is_ligado = False
            print('O veículo foi desligado!')

    @property   # O @property é usado para métodos que acessam e retornam propriedades da classe. Ao chamar o método, não precisamo usar os (), mas apenas o nome da propriedade. É uma forma elegante de acessar propriedades de uma classe.
    def qtd_combustivel(self):
        return self._qtd_combustivel

    # Definindo um método abstrato com a biblioteca abc.
    @abc.abstractmethod
    def pintar(self, cor):
        self._cor = cor