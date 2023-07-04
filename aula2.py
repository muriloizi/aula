
class Pessoa():
  def __init__(self,nome,idade):
    self.nome = "Jorge"
    self.idade = 24
  def seja(self):
    print("Seja bem vindo")

class Pessoafisica():
  def __init__(self,nome,idade,cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
  def seja(self):
    print("Seja bem vindo")

class Pessoajuridica():
  def __init__(self,nome,idade,cnpj):
    self.nome = nome
    self.idade = idade
    self.cnpj = cnpj
  def seja(self):
    print("Seja bem vindo")

#var = pessoajuridica()

class apres():
    def __init__(self):
      print("Seja bem vindo")
var= apres()

class PessoaFisica():

  def __init__(self,nome,idade,cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
  def seja(self):
    print("Seja bem vindo")
  def imposto(self,salario):
    taxa =0.015
    ir= salario*taxa
    return(ir)

puxar = PessoaFisica("jorge",29,123456789)
#puxar.imposto(6000)
valor= float(input("Quanto você ganha?\n"))
puxar.imposto(valor)

class PessoaJuridica():

  def __init__(self,nome,idade,cnpj):
    self.nome = nome
    self.idade = idade
    self.cnpj = cnpj
  def seja(self):
    print("Seja bem vindo")
  def imposto(self,salario):
    taxa =0.1
    ir= salario*taxa
    return(ir)

puxar = PessoaJuridica("jorge",29,123456789)
#puxar.imposto(6000)
valor= float(input("Quanto tu ganha safado?\n"))
puxar.imposto(valor)

class PessoaJuridica():

  def __init__(self,nome,idade,cnpj):
    self.nome = nome
    self.idade = idade
    self.cnpj = cnpj
  def seja(self):
    print("Seja bem vindo")
  def imposto(self,salario, taxa=0.10):
    ir = salario*taxa
    return ir

class Lar:
  def toctoc(self, pessoal=None, *pessoas):
    if pessoal is not None and pessoas is not None:
      for p in pessoas:
        print("Olá ", p)
    else:
      print("Quem está aí?")

batendoNaPorta = Lar()

class PessoaFisica():

  def __init__(self,nome,idade,cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
  def seja(self):
    print("Seja bem vindo")
  def imposto(self,*salario,taxa =0.015):
    print("Tupla de salario: ", salario)
    IR = 0
    #for s in salario:
    for s in range(len(salario)):
     ir = s*taxa
     IR = IR + ir

    print("O valor do seu imposto de renda é R$", IR)
    return IR

puxar = PessoaFisica("Paulo", 24, 123456789)
s =[]
while True:
    sal = float(input("salario: "))
    s.append(sal)
    op = int(input("ainda tem salario: 1-sim, 2-não "))
    if op == 1:
        continue
    else:
        tupla = tuple(s)
        print(s)
        break
       # valor= int(input("Quanto você ganha?\n"))
       # puxar.imposto(valor)
  
for i in range(len, (tuplas)):
  print(tupla[i])
  print(cliente.impostoderenda((tupla[i])))
class Pessoa():
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

class PessoaFisica(Pessoa):
  def __init__(self, nome, idade, cpf):
    super().__init__(nome,idade)
    self.cpf = cpf

def impostoDeRenda(self,faturamento,pE):
    if(pE==1):
        taxa = 0.10
    elif(pE==2):
        taxa = 0.15
    elif(pE==2):
        taxa = 0.20
        IR = faturamento*taxa
        return IR