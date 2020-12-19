def calcular_inss(salario):
    
    perc_75 = (1045 * 7.5)/100
    perc_9 = ((2089.60 - 1045) * 9)/100
    perc_12 = ((3134.40 - 2089.60) * 12)/100
    perc_14 = ((6101.06 - 3134.40)* 14)/100
    
    if salario <= 1045: 
            porcentagem_desconto_inss = (salario * 7.5)/100
            return round(porcentagem_desconto_inss , 2)  

    if salario >= 1045.01 and salario < 2089.60: 
            porcentagem_desconto_inss = (((salario - 1045) * 9)/100) + perc_75
            return round(porcentagem_desconto_inss , 2)  

    if salario >= 2089.61 and salario <= 3134.40: 
            porcentagem_desconto_inss = (((salario - 2089.60) *12)/100)+( perc_75 + perc_9)
            return round(porcentagem_desconto_inss , 2)  

    if salario >= 3134.41 and salario <= 6101.06: 
            porcentagem_desconto_inss = (((salario - 3134.40) * 14)/100) + (perc_75 + perc_9 + perc_12)
            return round(porcentagem_desconto_inss , 2)  
    else:
        porcentagem_desconto_inss = 713.10
        return porcentagem_desconto_inss 
        
# print(calcular_inss(6666.67))


