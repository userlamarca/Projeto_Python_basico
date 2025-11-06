def obter_dados_pessoais():
    print("-----Digite as suas informações abaixo-----")

    valor_nome = input("Nome: ")
    valor_cidade = input("Cidade: ")

    ano = 2025
    idade_valida = False
    
    while not idade_valida:
        valor_idade_str = input("Idade: ")
        
        try:
            idade_numerica = int(valor_idade_str)
            
            idade_valida = True
            
        except ValueError:
            print("ERRO: Por favor, insira um valor numérico válido para a idade.")
    
    
    ano_nascimento = ano - idade_numerica
    
    print("-----------------------------------")
    print(f"Olá {valor_nome}, você tem {idade_numerica} anos, nasceu em {ano_nascimento} e mora em {valor_cidade}.")

obter_dados_pessoais()