def calcular_inss(salario):
    
    perc_75 = (1100 * 7.5)/100
    perc_9 = ((2203.48 - 1100) * 9)/100
    perc_12 = ((3305.22 - 2203.48) * 12)/100
    perc_14 = ((6433.57 - 3305.22)* 14)/100
    
    if salario <= 1100: 
            porcentagem_desconto_inss = (salario * 7.5)/100
            return round(porcentagem_desconto_inss , 2)  

    if salario >= 1100.01 and salario < 2203.48: 
            porcentagem_desconto_inss = (((salario - 1100) * 9)/100) + perc_75
            return round(porcentagem_desconto_inss , 2)  

    if salario >= 2203.49 and salario <= 3305.22: 
            porcentagem_desconto_inss = (((salario - 2203.48) *12)/100)+( perc_75 + perc_9)
            return round(porcentagem_desconto_inss , 2)  

    if salario >= 3305.23 and salario <= 6433.57: 
            porcentagem_desconto_inss = (((salario - 3305.22) * 14)/100) + (perc_75 + perc_9 + perc_12)
            return round(porcentagem_desconto_inss , 2)  
    else:
        porcentagem_desconto_inss = 751.99
        return porcentagem_desconto_inss 
        
# print(calcular_inss(6666.67))


