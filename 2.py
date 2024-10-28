'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 
valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que 
desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
se o número informado pertence ou não a sequência.
'''

def fib(stop):
    a = 0
    b = c = 1
    next = b
    
    while c <= stop:
        print(next, end=" ")
        c += 1
        a, b = b, next
        next = a + b
    print()    

fib(10)
