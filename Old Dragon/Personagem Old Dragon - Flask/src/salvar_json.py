import json
import os

nome_arquivo = "personagens_Old_Dragon.json"

def salvar_personagem(personagem):
    personagens = carregar_personagens()
    personagens.append(personagem)
    with open(nome_arquivo, "w") as file:
        json.dump(personagens, file, indent=4)

def carregar_personagens():
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r") as file:
        return json.load(file)


