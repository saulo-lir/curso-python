import carro, moto, veiculo

# Instanciando a classe Carro
uno_vermelho = carro.Carro("Vermelho", 'Álcool', 1.0, 4)
uno_vermelho.ligar()
# del uno_vermelho (caso quisermos forçar a destruição do objeto antes do término da execução do script)
uno_vermelho.pintar('preto')

moto_vermelha = moto.Moto("Vermelha", 'Gasolina', 1.4, 2)
moto_vermelha.abastecer(20)
print(f"A quantidade de combustível da moto vermelha é {moto_vermelha.qtd_combustivel}")

# Verificar se o objeto 'moto_vermelha' é do tipo 'Veiculo'
if isinstance(moto_vermelha, veiculo.Veiculo):
    print("A classe é um veículo")
else
    print("A classe não é um veículo")