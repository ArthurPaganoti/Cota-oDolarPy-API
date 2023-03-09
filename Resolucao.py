# Exercicio utilizando API para pegar cotação do dolar
import requests
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
response = requests.get(url)
valor_real = float(input('Digite o valor em R$'))
if response.status_code == 200:
    dolar_value = float(response.json()['USD']['ask'])
    valor_total = valor_real/dolar_value
    print(f'O valor do dolar em R$ nesse exato momento é {dolar_value}')
    print(f'O valor do R${valor_real} em U$ é {valor_total}')
else:
    print('Erro ao buscar o valor do dolar')