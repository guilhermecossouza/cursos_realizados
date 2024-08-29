import urllib3
try:
    resposta = urllib3.request("GET", "http://www.pudim.com.br/")
    print(resposta) 
except Exception as erro:
    print(f"Site não encontrado {erro.__cause__}")
