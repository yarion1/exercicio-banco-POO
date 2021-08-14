class Cliente():
    def __init__(self,nome=None,cpf=None,idade=None):
        if(nome==None):  
            self.nome=""
        else:
            self.nome=nome
        if(cpf==None):
            self.cpf=0
        else:
            self.cpf=cpf
        if(idade==None):
            self.idade=""
        else:
            self.idade=idade


    def setnome(self,nome):
        self.nome=nome

    def setcpf(self,cpf):
        self.cpf=cpf

    def setidade(self,idade):
        self.idade=idade

    def getnome(self):
        return self.nome
    
    def getcpf(self):
        return self.cpf

    def getidade(self):
        return self.idade
        
    
    def cadastracliente(self, newCpf):
        self.nome=input("Digite o nome:")
        self.cpf= newCpf
        self.idade=int(input("Digite a Idade:"))
    
    def mostracliente(self):
        print("Nome: ",self.nome,"CPF: ",self.cpf,"Idade: ",self.idade)


class Conta():
    def __init__(self, cpf=None, nome=None, Nconta=None, Saldo=None):
        if cpf == None:
            self.cpf=0
        else:
            self.cpf = cpf
        if nome == None:
            nome=""
        else:
            self.nome=nome
        if Nconta == None:
            Nconta = 0
        else:
            self.Nconta=Nconta
        if(Saldo == None):
            self._Saldo=0.00
        else:
            self._Saldo = Saldo
    
    def cadastraconta(self, cpf, nome):
        self.nome=nome
        self.cpf=cpf
        self.Nconta=int(input('Insira o numero da nova conta: '))
        self._Saldo=0.00

    def mostraconta(self):
        print("Nome: ",self.nome,"CPF: ",self.cpf,"Nconta: ",self.Nconta,"Saldo: ",self._Saldo) 
    
    def deposita(self):
        valor = float(input('Insira qual valor deseja depositar: '))
        novoSaldo = self._Saldo + valor
        self._Saldo = novoSaldo

    def saque(self):
        valor = float(input('Insira qual valor deseja sacar: '))
        if valor > self._Saldo:
            print('O valor digitado é superior ao seu saldo atual')
        elif valor == 0:
            print('o valor minimo de saque é 2 reais')
        else:
            novoSaldo = self._Saldo - valor
            self._Saldo = novoSaldo
            print('Saque realizado com sucesso! Retire as notas e o comprovante no terminal.')

    def transf(self):
      valor = float(input('Insira o valor a ser trasnferido'))
      if self._Saldo < valor:
        print('Você não possui saldo para realizar a operação')
      else:
        self._Saldo -= valor
        return valor


class ContaEspecial(Conta):
    def __init__(self, cpf, nome, Nconta , Saldo, limite):
        super().__init__(cpf, nome , Nconta, Saldo)
        self.limite = limite
        self._Saldo= limite
    def saque(self):
        valor = float(input('Digite o valor do saque na conta especial: '))
        if (self._Saldo + self.limite) < valor:
            print("Você não possui limite especial suficiente para esta operação!")
        else:
            print('Saldo: {}',self._Saldo)
            self._Saldo = (self._Saldo - valor)
            return self._Saldo
    
    def mostrarSaldo(self):
        print("Limite dissponivel  na conta especial: ",self._Saldo)




