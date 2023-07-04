listaDeContatos = {"diana":978789789798,"Lidiane":15648743,"Larissa":456138431,"Rayane":1345613545,"Julia e Joeyce":15165135186,"Larissa2":1234864531,"Samuel":231861351,"Felipe":15341561,"Ryan":165461531,"Thiago":6548624646,}


def buscarNoTelefone(nome):
    if nome in listaDeContatos:
        print("O telefone é: ", listaDeContatos[nome])
