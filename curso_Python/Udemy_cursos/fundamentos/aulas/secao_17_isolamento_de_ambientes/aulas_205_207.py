# aula 205 Introdução do Módulo
# venv é um conjuto resumido do virtual env
# A partir do python 3.3 a venv vio nativo na instalação do python
# foi criado uma pasta chamada projeto_teste para fazermos o isolamento.
# -==================================================================================================
# aula 206 Comando de Ativação do venv no Windows
# Comando de Ativação do venv no Windows
# O comando que é mostrado durante a próxima aula não está mais funcionando no Windows, o novo comando é:
# .venv\Scripts\activate
# Bons estudos!
# ======================================================================================================
# Aula 207 venv
# acesse a pasta criada projeto_teste
# para criar um venv python -m venv <nome da pasta> ele irá criar essa pasta com as dependências do pyrhon ,
# a partir da í os pacotes instalado serão instalados nessas dependências
# para ativar a venv digite .\venv\Scripts\activate.ps1
# caso der erro digite
# obs:
# Abra um powerShell como administrador
# digite o comando:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# Para mostrar o caminho da venv
# echo $VIRTUAL_ENV
# para verificar onde sera feita a busca dos pacores seperados
# python -c 'import sys; print(sys.path)'
# ['',
# 'C:\\Users\\Zaca-prova-facil\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip',
# 'C:\\Users\\Zaca-prova-facil\\AppData\\Local\\Programs\\Python\\Python311\\DLLs',
# 'C:\\Users\\Zaca-prova-facil\\AppData\\Local\\Programs\\Python\\Python311\\Lib',
# 'C:\\Users\\Zaca-prova-facil\\AppData\\Local\\Programs\\Python\\Python311',
# 'C:\\Users\\Zaca-prova-facil\\Documents\\exercicio_python\\curso_udemy\\fundamentos\\aulas\\secao_17_isolamento_de_ambientes\\projeto_teste\\venv',
# 'C:\\Users\\Zaca-prova-facil\\Documents\\exercicio_python\\curso_udemy\\fundamentos\\aulas\\secao_17_isolamento_de_ambientes\\projeto_teste\\venv\\Lib\\site-packages'
# ]
# para instalar os pacoter a partir do requirements.txt : pip install -r requirements.txt
# para sair da venv é só digitar deactivate
