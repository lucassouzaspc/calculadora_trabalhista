import inss as inss
import irpf as irpf
import ferias as ferias
import plr as plr 
import salario_liquido as sl

def calculadora():      
      while True:

            
            print(""" \n====== Menu de Opções: =======\n
                  0. Calcular desconto INSS
                  1. Calcular desconto IRPF
                  2. Calcular desconto Férias
                  3. Calcular desconto PLR
                  4. Calcular desconto Salário
                  5. Sair
                  """)
            try:
                  opcao = int(input("Escolha uma opção do menu. (Exemplo: 1)  : "))
                  if opcao not in range(0,6):
                        print('\nEscolha uma opção válida da lista do menu!')
                        continue

                  elif opcao == 5:
                        raise SystemExit      
                  
            except ValueError:
                  print('\nEscolha uma opção válida da lista do menu!')
                  continue           


            while True:
                 
                  try:
                        salario = float(input("Digite o valor a ser calculado: "))
                        break
                  except:
                        print('Digite um valor númerico (Exemplo: 3500 ou 3500.98)')
                        continue
            
            if opcao == 0:
                  desconto_inss = inss.calcular_inss(salario)
                  print('\nSerá descontato R$:',desconto_inss,'\nTotal Líquido R$:',(salario - desconto_inss))

            elif opcao == 1:
                  desconto_irpf = irpf.calcular_ir(salario)
                  print('\nSerá descontato R$:',desconto_irpf,'\nTotal Líquido R$:',(salario - desconto_irpf))

            elif opcao == 2:
                  terco_salario = round((salario /3),2)
                  salario_bruto = terco_salario + salario
                  desconto_ferias = ferias.calcular_ferias(salario)
                  print('\nSerá descontato R$:',desconto_ferias,'\nTotal Líquido R$:',(salario_bruto - desconto_ferias))                

            elif opcao == 3:
                  desconto_plr = plr.calcular_plr(salario)
                  print('\nSerá descontato R$:',desconto_plr,'\nTotal Líquido R$:',(salario - desconto_plr))                

            elif opcao == 4:
                  salario_atual = sl.Salario(salario)
                  salario_atual.descontos()
                  desconto_salario_liquido = salario_atual.salario_liquido()
                  print('\nSerá descontato R$:',round(salario - desconto_salario_liquido),2 ,'\nTotal Líquido R$:',desconto_salario_liquido)
                  

            else:
                  print('\nEscolha uma opção válida do menu!')
                  continue                  
