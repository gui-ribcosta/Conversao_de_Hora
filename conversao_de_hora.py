n = 1
A = 'A.M'
P = 'P.M'

while n != 0:

    def conversao(hora, conversao):

        if hora <= 12:
            conversao = hora
            return conversao

        if hora > 24:
            conversao = hora - 24
            return conversao

        if hora > 11:
            conversao = (hora + 12) - 24
            return conversao


    def resultado(resultado):

        resultado = (f"Conversão: \033[7m{conversao(hora, conversao)}:{min} {periodo}\033[m")
        return resultado


    hora = int(input("Digite a hora: "))

    if hora < 0:
        break


    if hora > 24:
        print("Valor Inválido,Digite novamente!")
        continue

    min = int(input("Digite o minuto: "))

    if min < 0 or min > 59:
        print("Valor Inválido,Digite novamente!")
        continue

    if hora <= 11:
        periodo = A

    else:
        periodo = P

    print(resultado(resultado))