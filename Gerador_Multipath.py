"""[Descrição]:
OBJ: Automatizar criação de arquivos de configurações Multipaths
de forma linear usando metodologia de iteração.

Responsável: Ihan Messias Nascimento dos Santos
Gmail: ihanmessias.dev@gmail.com
GitHub: https://github.com/mrhowaito
Linkedin: https://www.linkedin.com/in/ihanmessias/
Contato: +55 (61) 99648-7935

Versão: Beta 0.4 | Data de Criação: 15/08/2022
Versão da linguagem: Python 3.10.4
"""

import os # Biblioteca de Manuseio de Sistemas Operasionais
    
while True: # Aplicando Loop para checagem de dados
    check_multipath = 'multipath.config' # Armazenado variável principal
    try: # Tenta executar (Tratamento de Erro)
        if os.path.isfile(check_multipath): # Faz a verificação do arquivo "multipath.config", caso já exista move para o diretório "/tmp"
            os.system(f"mv {check_multipath} /tmp") # Movendo arquivo já existente "multipath" para "/tmp"
        else: # Caso o arquivo não exista no diretório atual, faz criação dos dependentes.
            os.system('multipathd show maps format "%n %w %d %s %S" > background.config') # Captura dados em arquivo backgound.config
            with open("background.config","r",encoding="utf-8") as file: # Faz a leitura do arquivo e codifica em parâmetro "utf-8"
                multpaths = file.readlines() # Armazena leitura de todas as linhas em variável

            os.system('hostname > hostname.config') # Captura dados de hostname da máquina em "hostname.config"
            with open("hostname.config","r",encoding="utf-8") as file: # Faz a leitura do arquivo e codifica em parâmetro "utf-8"
                hostname = file.readline() # Armazena leitura de linha unica em variável

            hostname = (hostname.split()) # Trasforma String em lista
            count = 0 # Faz a contagem para nomear iterações

            for lines in multpaths: # Faz iteração para cada linha no arquivo "backgound.config"
                output = lines.split() # Tranforma cada linha em lista
                if len(output[1]) == 33: # Verifica se o índice "1" da lista contém 33 caracteres.
                    with open(check_multipath,"a",encoding="utf-8") as file: # Faz a adção e codifica em parâmetro "utf-8"
                        file.write("multipath {\n        wwid %s\n        alias mpath_%s_ora_asm_0%s\n}\n" % (output[1],hostname[0],count)) # Escreve e implementa formatação.

                    count += 1 # Soma para proceguir com Contagem
                else: # Caso o índice "1" não tenha 33 caracteres
                    continue # continua com o processo de iteração normalmente

            if os.path.isfile(check_multipath): # Verifica de arquivos "background.config" e "hotname.config" existe
                os.system("mv background.config /tmp") # Move "background.config" para o diretório "/tmp"
                os.system("mv hostname.config /tmp") # Move "hostname.config" para o diretório "/tmp"
            
                print(f'Arquivo {check_multipath} criado com sucesso.') # Apresenta ao usuario a criação do arquivo
                break # Faz a interrupção do Loop
            else:
                print("multipathd não encontrado")
                break # Faz a interrupção do Loop

    except KeyboardInterrupt: # Tratamento de erro em caso de "CTRL+C" (Caso Script Trave)
        print('\nABORTADO!') # Apresenta ao usuario a interrupção da execução do programa
        exit() # Finaliza Script