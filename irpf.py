import inss as inss


def calcular_ir(salario):

    base_calculo_ir = salario - inss.calcular_inss(salario)
    
    while True:
        try:
            dependentes = int(input('Possui quantos dependentes: '))
            break
        except:
            print('Digite um valor inteiro Exemplo: 0 ')
            continue

    dependentes = dependentes * 189.59
    base_calculo_ir = base_calculo_ir - dependentes

    if base_calculo_ir <= 1903.98:
        return 0

    if base_calculo_ir >= 1903.99 and base_calculo_ir < 2826.65:
        porcentagem_desconto_ir = 7.5
        deducao_imposto = 142.80

    if base_calculo_ir >= 2826.66 and base_calculo_ir < 3751.05:
        porcentagem_desconto_ir = 15
        deducao_imposto = 354.80

    if base_calculo_ir >= 3751.06 and base_calculo_ir < 4664.68:
        porcentagem_desconto_ir = 22.5
        deducao_imposto = 636.13

    if base_calculo_ir >= 4664.68:
        porcentagem_desconto_ir = 27.5
        deducao_imposto = 869.36

    return round((base_calculo_ir * porcentagem_desconto_ir / 100.0) - deducao_imposto, 2)

# print(calcular_ir(6666.67))
