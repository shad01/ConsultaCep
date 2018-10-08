import requests

def request():
    cep = str(input("Cep: ")).replace("-", "")
    while len(cep) < 8 or len(cep) > 8:
        cep = str(input("Cep: ")).replace("-", "")

    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    r_dict = resposta.json()
    print()

    for key, value in r_dict.items():
        if key == "erro":
            print("Cep Inválido")

        elif value == "":
            print(f"{key}: Sem Informação")

        else:
            print(f"{key}: {value}")

request()
