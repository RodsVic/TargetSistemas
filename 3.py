'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser 
ignorados no cálculo da média;
'''
import json

def func():
    with open ("dados.json", "r", encoding="utf-8") as file:
        dados = json.load(file)
        soma = max = dias_validos = superior = 0
        min = 99999999
        for i in dados:
            if i["valor"] != 0:
                soma += i["valor"]
                dias_validos += 1
                
                if i["valor"] > max:
                    max = i["valor"]
            
                if i["valor"] < min:
                    min = i["valor"]
                           
        media = soma / dias_validos    
        
        for i in dados:
            if i["valor"] > media:
                superior += 1
                
        print(f"Menor valor no mês: {min:.2f}\nMaior valor no mês: {max:.2f}")
        print(f"Dias superiores a meta: {superior}")

func()