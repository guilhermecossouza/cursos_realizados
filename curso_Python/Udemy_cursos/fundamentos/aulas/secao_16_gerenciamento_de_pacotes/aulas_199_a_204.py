# Aula 199 Introdução do Módulo
# https://pypi.org/ para baixar pacotes do python
# Nele irá conter os pacotes e o comando para instalaão como o comando pip
# ==========================================================================================
# 200. Conferindo Versões e PIP Upgrade
# Verificar a versão do Python
# python --version
# python3 --version
# Verificar a verção do pip
# pip --version
# Caso esse comando não o resultado for não encontrado tem outras formas
# execute o comando:
# python -m pip --version
# O python -m ele vai executar o comando como um script [ pip --version ]
# Caso tenha o pip3 use o camando
# pip3 --version
# No caso aqui o pip3 é um elias [ um apelido ]
# A partir da versão 3.4 o pip já vem istalado junto com o python.
# Para atualizar o pip3 install --upgrade pip
# ============================================================================================
# Aula 201 Erro do PIP Search
# O comando de busca  pip3 search foi descontinuado
# =============================================================================================
# 202 pip
# pip3 --help mosta uma lista de comandos para usar no pip
# pip3 <command> [options]
# pip3 install --help
# pip3 search django DESCONTINUADO
# ERRO:
# ERROR: XMLRPC request failed [code: -32500]
# RuntimeError: PyPI no longer supports 'pip search' (or XML-RPC search). Please use https://pypi.org/search (via a browser) instead.
# See https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods for more information.
# pip3 list -> lista os pacotes instalados
# python -m site
# lista as paths aonde o python pesquisa os pacotes instalados
# pip install django -> instalando o pacote django vai ter alterações em pastas compartilhadas, povavelmente irá dar uma erro por causa disso
# pip3 install --user django -> instalando o django na pasta de usuário vai alterar somente as pastas do seu usuário aonde vc tem permissão
# com o pacote django instalado e configurado na máquina pode executar o comando python -c para executar um trecho de cósigo dentro da statring
# python -c "import djnago;" podendo executar mais um de trecho de código separados por ;
# <module 'django' from 'C:\\Users\\Zaca-prova-facil\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\django\\__init__.py'>
# Para desinstalar o pcote django ou qualquer outro
# pip 3 uninstall <pacote>
# pip3 uninstall django
# ===============================================================================================================================================
# aula 203 Congelar Pacotes
# pip3 freeze vai listar todos os pacotes instalados e suas verões
# asgiref==3.7.2
# flake8==6.1.0
# mccabe==0.7.0
# pycodestyle==2.11.1
# pyflakes==3.1.0
# sqlparse==0.4.4
# tzdata==2023.3
# urllib3==2.1.0
# foi criado uma pasta de nome pip, para ser criado o requirements.txt
# vamos acessar essa pasta
# cd .\curso_udemy\fundamentos\aulas\secao_16_gerenciamento_de_pacotes\pip\ (windows)
# pip3 freeze > requirements.txt -> vai pegar os pacotes instalados mostrados no comando pip3 freeze e passar todos para esse .txt em forma de texto
# asgiref==3.7.2 isso será usado para instalar os pacotes em outra máquina
# para instalar os pacotes descritos no requirements.txt executar o comando
# pip3 install -r requirements.txt -> r = leitura
# para escrever no terminal use o comando echo "texto"
# echo "django==5.0"
# esse comando também pode ser usado para escrever em arquivos desde que vc esteja na mesma pasta do arquivo
# echo "django==5.0" >> requirements.txt
# o pip trabalha de duas formas instala os pacotes no global ou na pasta de ususario
# pip3 install django
# pip3 install --user django
# para verificar se tem algum pacote desatualizado
# pip3 list --outdated
# para atualizar o pacote
# pip3 install --upgrade
# -===================================================================================================================================
# aula 204 Conclusão do Módulo
# comandos na apostila
