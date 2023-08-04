def caixa(valor):
    if(valor < 10 or valor > 600):
        return print("Valor inválido")
    
    notas = [100,50,10,5,1]
    qtde = [0,0,0,0,0]
    i = 0

    while(valor > 0):
        if (notas[i] <= valor):
            valor -= notas[i]
            qtde[i] += 1
        else:
            i += 1
    

    for i in range(len(notas)):
        print(f"{qtde[i]} notas de {notas[i]} Dólar(es)")
        





