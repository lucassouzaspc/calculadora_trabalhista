import inss as inss
import irpf as irpf
import ferias as ferias
import plr as plr


class Salario:
    
    def __init__(self, salario):
        
        self.salario = salario
        self.IPRF = irpf.calcular_ir(self.salario)

    def __str__(self):
        
        return f'{self.salario}'
        

    def descontos(self):


        while True:
             
              try:
                    self.VR = float(input('Digite o valor do descontado do Vale Refeição: '))
                    break
              except:
                    print('Digite um valor númerico Exemplo: 13.00')
                    continue
        
        while True:
             
              try:
                    self.academia = float (input('Digite o valor do descontado da academia: '))
                    break
              except:
                    print('Digite um valor númerico Exemplo: 13.00')
                    continue        
        while True:
             
              try:
                    self.unimed = float (input('Digite o valor do descontado do Plano de Saúde: '))
                    break
              except:
                    print('Digite um valor númerico Exemplo: 13.00')
                    continue          
        while True:
             
              try:
                    self.dental = float (input('Digite o valor do descontado do plano dental: '))
                    break
              except:
                    print('Digite um valor númerico Exemplo: 13.00')
                    continue           
        
        while True:
             
              try:
                    self.outros_descontos = float (input('Digite o valor de Outros Descontos: '))
                    break
              except:
                    print('Digite um valor númerico Exemplo: 13.00')
                    continue
                

        self.INSS = inss.calcular_inss(self.salario)
        self.IPRF = self.IPRF

        self.descontos = float(self.VR + self.academia + self.unimed + self.dental + self.outros_descontos + self.INSS + self.IPRF)

        return self.descontos
    
    def salario_liquido(self):
        self.salario_liquido = float((self.salario) - (self.descontos))

        return round(self.salario_liquido , 2)  
