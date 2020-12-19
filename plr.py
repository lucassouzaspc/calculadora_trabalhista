def calcular_plr(valor_plr):

	base_calculo_plr = valor_plr

	if base_calculo_plr <= 6677.55:
		return 0

	elif base_calculo_plr >= 6677.56 and base_calculo_plr < 9922.28: 
		porcentagem_desconto_plr = 7.5
		deducao_imposto = 500.82

	elif base_calculo_plr >=  9922.29 and base_calculo_plr < 13167.00: 
		porcentagem_desconto_plr = 15
		deducao_imposto = 1244.99

	elif base_calculo_plr >= 13167.01 and base_calculo_plr < 16380.38: 
		porcentagem_desconto_plr = 22.5
		deducao_imposto = 2232.51

	elif base_calculo_plr >= 16380.38: 
		porcentagem_desconto_plr = 27.5
		deducao_imposto = 3051.53

	return round(((base_calculo_plr * porcentagem_desconto_plr / 100.0) - deducao_imposto) , 2)


##print(calcular_plr(8600.00))

