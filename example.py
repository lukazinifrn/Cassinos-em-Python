import roulette

game1 = roulette.Gambling({"a" : 10, "b" : 20, "c": 80}, 4)

'''
Explicação:
Definimos 3 items  "a", "b" e "c", todos tem suas respectivas chances: 10, 20, 80
Ou seja, o "c" tem uma maior chance de aparecer, pois possui 80% de chance, enquanto
o "a" tem apenas 10%

O segundo argumento se refere ao tamanho que a lista terá, ou seja, se o valor for 3
a lista será do tipo [item1, item2, item3]
'''

game1_result = game1.result_list()

'''
Explicação:
Executa a função dentro do módulo que gera uma lista com base nos valores anteriormente
descritos, ou seja, o dicionário com os valores e suas chances, e o tamanho que a lista deve 
possuir
'''
