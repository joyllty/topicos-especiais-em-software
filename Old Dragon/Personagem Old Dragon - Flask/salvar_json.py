import json
import os

nome_arquivo = "personagens_Old_Dragon.json"

def salvar_personagem(personagem_obj):
    """
    Recebe uma Instância de objeto Personagem.
    Converte para dicionário usando __dict__ e salva no JSON.
    """
    
    # não quebrar o objeto original que o Flask ainda está usando
    personagem_dict = personagem_obj.__dict__.copy()

    # convertendo os objetos para o nome da classe 
    if personagem_dict.get("raca"):
        personagem_dict["raca"] = personagem_dict["raca"].__class__.__name__
        
    if personagem_dict.get("classe"):
        personagem_dict["classe"] = personagem_dict["classe"].__class__.__name__
        
    # remover o objeto Dado
    if "dado" in personagem_dict:
        del personagem_dict["dado"]
        
    personagens = carregar_personagens()
    personagens.append(personagem_dict)
    
    with open(nome_arquivo, "w") as file:
        json.dump(personagens, file, indent=4)

def carregar_personagens():
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []