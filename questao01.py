from moduloq01 import *


listausuarios = []
listaConta = []

def menuconta(cpf): 
    flag = 0
    print("\n\nA Conta Atual é:")
    for U in listausuarios:
      if U.cpf == cpf:
        print('Bem vindo, {}!\n'.format(U.nome))
        U.mostracliente
        for C in listaConta:
          if C.cpf == cpf:
            C.mostraconta()
            flag = 1
        if flag == 0:
          print('O usuário ainda não possui uma conta!\n')
          print('iniciando cadastro de conta!\n')
          continuar = input("Pessione <Enter> para Continuar")
          novaconta = Conta()
          novaconta.cadastraconta(cpf, U.nome)
          listaConta.append(novaconta)
          flag = 0
          cs = str(input('Cadastrar conta especial? [S/N]: '))
          novas_contas = ContaEspecial(None, None, None, None, None)
          if cs == 'S' or cs == 's':
              limite = float(input('Insira o limite desejado para a conta especial: '))
              novas_contas =  ContaEspecial(novaconta.cpf, novaconta.nome, novaconta.Nconta, novaconta._Saldo, limite)

    print("\n\n")
    continuar = input("Pessione <Enter> para Continuar")

    op=0

    while op!=-1:
      Contaa = Conta()
      for U in listausuarios:
        if U.cpf == cpf:
          print('Bem vindo, {}!\n'.format(U.nome))
          U.mostracliente
          for C in listaConta:
            if C.cpf == cpf:
              C.mostraconta()
              Contaa = C

      print('''  
      -------------BANCO----------------
          1[Depósito]
          2[Saque]
          3[Saldo]
          4[saque Conta Especial]
         -1[Sair]
     --------------------------------
     ''')
      op=int(input("   \n->"))

      if(op == -1):
        break
      elif op == 1:
          Contaa.deposita()
          if novas_contas._Saldo != None:
            novas_contas._Saldo = (limite - Contaa._Saldo)
      elif op == 2:
        Contaa.saque()
      elif op == 3:
        ContaEspecial.mostrarSaldo(novas_contas) 
      elif op==4:
        if novas_contas._Saldo == None:
          print('O usuário não possui conta especial')
        else:
          auxSaldo = ContaEspecial.saque(novas_contas)
          defCred = (limite - auxSaldo)
          Contaa._Saldo -= defCred
      elif op==5:
        auxDest = 0
        dest=int(input("insira a numero da conta do destinatario: "))
        for ntransf in listaConta:
          if (ntransf.Nconta == dest):
            print('a conta selecionada foi:\n')
            print("Nome:{}\nCpf:{}\nConta:{}\n".format(ntransf.nome, ntransf.cpf, ntransf.Nconta))
            cont = str(input('Deseja continuar com a transferencia? [S/N]'))
            if cont == 'S' or cont == 's':
              valTransf = Contaa.transf()
              ntransf._Saldo = (ntransf._Saldo + valTransf)
            auxDest = 1
        if auxDest != 1:
          print("a conta inserida nao foi encontrada!")
      
      else: 
        print('opcao invalida!')
    

op=0

while op!=-1:
    print('''  
    ----------MENU-----------  
      1[Cadastro Usuario]
      2[Lista Usuario]
      3[Entrar na Conta]
     -1[Sair]
    -------------------------
     ''')
    op=int(input("   ->"))

    if(op == 1):
      verCli = 0
      newClient = Cliente()
      newCpf =int(input('Insira o cpf do novo cliente: '))
      for C in listausuarios:
        if C.cpf == newCpf:
            print('cpf existente, usuário já cadastrado')
            verCli = 1
      if verCli == 0:
          newClient.cadastracliente(newCpf)
          listausuarios.append(newClient)
    elif op == 2:
      for cli in listausuarios:
        cli.mostracliente()
    elif op == 3:
      cpf = int(input("Digite o cpf do usuário para acessar a sessão contas: "))
      menuconta(cpf)
    else:
      print('opção invalida')