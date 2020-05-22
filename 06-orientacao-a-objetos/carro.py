import veiculo

# Para fazermos a herança, devemos atribuir a class mãe como parâmetro na classe filha.
class Carro(veiculo.Veiculo):   # Dessa forma, estamos dizendo que a classe Carro é do tipo Veiculo

    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia) # Acessando os atributos presentes no construtor da classe pai
        self.qtd_portas = qtd_portas

    # Aplicando o polimorfismo reescrevendo o método da classe pai
    def abastecer(self, qtd_combustivel):
        print('O método foi chamado a partir da classe Carro')
        self.__qtd_combustivel += qtd_combustivel

    # Implementando o método abstrato pintar (Obrigatório, pois a classe Carro está herdando de uma classe abstrata)
    def pintar(self, cor):
        if cor == "preto":
            print("O carro não pode ser preto")
        else:
            self._cor = cor
