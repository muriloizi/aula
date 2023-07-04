class Pessoa():
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def getNome(self):
    return self.__nome
   
  def setNome(self, novoNome):
    self.__nome = novoNome
    
  def apresentacao(self):
   print("\nSeja bem vindo\n")


class PessoaFisica(Pessoa):
  def __init__(self, nome, idade, cpf):
    super().__init__(nome,idade)
    self.cpf = cpf
  
  def ir(self, *salarios, taxa=0.015):
    irTotal = 0
    for salario in salarios:
      IR_i =salario * taxa
      irTotal = irTotal + IR_i
    return irTotal

class Pessoajuridica():
  def __init__(self,nome,idade,cnpj):
    self.nome = nome
    self.idade = idade
    self.cnpj = cnpj
  def seja(self):
    
    print("Seja bem vindo")
  def impostoDeRenda(self,faturamento,pE):
    if(pE==1):
        taxa = 0.10
    elif(pE==2):
        taxa = 0.15
    elif(pE==3):
        taxa = 0.20
    IR = faturamento*taxa
    return IR

nome = input("Coloque seu nome: ")
idade = int(input("Coloque sua idade: "))
cliente = Pessoa(nome, idade)
cliente.apresentacao()
usuario = int(input("Veja os dois casos\n1 para Pessoa Fisica\n2 para Pessoa Juridica\nDigite qual deles é seu caso: "))
if(usuario==1):
  cpf=int(input("CPF: "))
  salario = int(input("Digite agora seu salario: "))
  clienteF = PessoaFisica(nome, idade, cpf)
  print(clienteF.ir(salario))
  
elif(usuario==2):
  cnpj=int(input("CNPJ: "))
  clienteJ = Pessoajuridica(nome, idade, cnpj)
  salario = int(input("Digite agora seu salario: "))
  pE= int(input("""
+===================+
| Porte da Empresa  |
| 1 - Pequeno Porte |
| 2 - Medio Porte   |
| 3 - Grande Porte  |  
+===================+             
 Qual porte da sua empresa? """))
  print(clienteJ.impostoDeRenda(salario, pE))
  
else:
  input("valor invalido, reinicie o aplicativo")




#cliente = PessoaFisica("Murilo",24,465456453)
#empresa = Pessoajuridica("Bradesco", 15, 48646426)
#porteDaEmpresa = int(input("""
#+===================+
#| Porte da Empresa  |
#| 1 - Pequeno Porte |
#| 2 - Medio Porte   |
#| 3 - Grande Porte  |  
#+===================+             
# """))
##porteDaEmpresa = int(input())
#print(empresa.impostoDeRenda(100000, porteDaEmpresa))