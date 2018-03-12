def converte_dois_digitos(vetor, ind1, ind2, base):
    x = (vetor[ind1] + vetor[ind2])
    y = int(x, base)
    return y

def converte_tres_digitos(vetor, ind1, ind2, ind3, base):
    x = (vetor[ind1] + vetor[ind2] + vetor[ind3])
    y = int(x, base)
    return y

def operacao():
    vetor = []
    final = 1

    while(not final):
        juncao = converte_dois_digitos(vetor, 0, 1, 2)
        if (juncao == 2):
            op = "add"

        operador1 = converte_tres_digitos(vetor, 2, 3, 4, 2)
        operador2 = converte_tres_digitos(vetor, 5, 6, 7, 2)

        resultado = operador1 + operador2
        resultado_binario = int(resultado, base=10)
        
        posicao = converte_tres_digitos(vetor, 8, 9, 10, 2)



if(__name__ == "__main__"):
    operacao()
