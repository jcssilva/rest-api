import json, requests
import moedas


#response = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='08-07-2019'&$top=100&$format=json")
response = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='08-07-2019'")
#print(response.content)
moedas = json.loads(response.content)

print('R$ ' +  str(moedas['value'][0]['cotacaoCompra']))

# for moeda in moedas['value']:
#     print("Símbolo: " + moeda['simbolo'])
