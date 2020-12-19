import inss as inss
import irpf as irpf
def calcular_ferias(salario):
    	
	terco_salario = round((salario /3),2)
	salario_bruto = terco_salario + salario
	desconto_inss = inss.calcular_inss(salario_bruto)
	desconto_ir = irpf.calcular_ir(salario_bruto)
	descontos = desconto_inss + desconto_ir
	valor_ferias = (salario_bruto - descontos)
	return round((descontos) , 2)


# print(calcular_ferias(5000))