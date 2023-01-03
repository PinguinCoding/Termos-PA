qntdTermos = 10
primeiroTermo = int(input("Insira o primeiro termo: "))
razaoPA = int(input("Insira a razão: "))
termoLimite = primeiroTermo + (qntdTermos-1) * razaoPA
continuarPA = True
proximoTermo = primeiroTermo
print(primeiroTermo, end =' ')
while continuarPA:

    while proximoTermo != termoLimite:
        proximoTermo += razaoPA
        print(proximoTermo, end=' ')

    qntdTermosAmais = int(input("\nInsira quantos termos deseja ver agora: "))
    qntdTermos += qntdTermosAmais
    termoLimite = primeiroTermo + (qntdTermos-1) * razaoPA

    if qntdTermosAmais == 0:
        continuarPA = False
