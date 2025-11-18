from flask import Blueprint, render_template, request
from model.personagem import Personagem
from model.racas.Humano import Humano
from model.racas.Elfo import Elfo
from model.racas.Anao import Anao
from model.classes.Necromante import Necromante 
from model.classes.Druida import Druida 
from model.classes.Paladino import Paladino
from salvar_json import salvar_personagem, carregar_personagens

blueprint_personagem = Blueprint("personagem", __name__)

@blueprint_personagem.route("/criar", methods=["GET", "POST"])
def criar_personagem():
    atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

    # ===== distribuição manual (aventureiro ou heroico) =====
    if "valor_0" in request.form:
        # Reconstruir personagem a partir de hidden inputs -> quando chegava na distribuição, como são POST's independentes, o personagem era criado de novo e retornava nulo 
        personagem = Personagem()
        personagem.nome = request.form.get("nome")
        raca = request.form.get("raca")
        classe = request.form.get("classe")

        personagem.raca = {"Humano": Humano(), "Elfo": Elfo(), "Anao": Anao()}[raca]
        personagem.classe = {"Necromante": Necromante(), "Paladino": Paladino(), "Druida": Druida()}[classe]

        # recuperar valores gerados
        valores_gerados = [int(v) for v in request.form.get("valores_gerados").split(",")]

        personagem.valores_gerados = valores_gerados

        distribuicao = {}
        usados = []
        for i in range(len(valores_gerados)):
            attr_escolhido = request.form.get(f"valor_{i}")
            if attr_escolhido not in usados:
                distribuicao[attr_escolhido] = valores_gerados[i]
                usados.append(attr_escolhido)

        personagem.distribuir_atributos(distribuicao)

        salvar_personagem(personagem.to_dict())

        return render_template(
            "criar_personagem.html",
            personagem=personagem,
            etapa="exibir",
            habilidades_classe=personagem.classe.exibir_habilidades_classe(),
            habilidades_raca=personagem.raca.exibir_habilidades_raca()
        )

    # ===== envio inicial de dados =====
    if request.method == "POST":
        personagem = Personagem()
        personagem.nome = request.form.get("nome")
        raca_escolhida = request.form.get("raca")
        classe_escolhida = request.form.get("classe")
        estilo = request.form.get("estilo")


        personagem.raca = {"Humano": Humano(), "Elfo": Elfo(), "Anao": Anao()}[raca_escolhida]
        personagem.classe = {"Necromante": Necromante(), "Paladino": Paladino(), "Druida": Druida()}[classe_escolhida]

        if estilo == "classico":
            personagem.estilo_classico()
            salvar_personagem(personagem.to_dict())
            return render_template(
                "criar_personagem.html",
                personagem=personagem,
                etapa="exibir",
                habilidades_classe=personagem.classe.exibir_habilidades_classe(),
                habilidades_raca=personagem.raca.exibir_habilidades_raca()
            )

        elif estilo in ["aventureiro", "heroico"]:
            if estilo == "aventureiro":
                valores = personagem.estilo_aventureiro()
            else:
                valores = personagem.estilo_heroico()
            
            personagem.valores_gerados = valores 

            return render_template(
                "criar_personagem.html",
                personagem=personagem,
                valores=valores,
                atributos=atributos,
                etapa="distribuir",
                hidden_nome=personagem.nome,
                hidden_raca=raca_escolhida,
                hidden_classe=classe_escolhida,
                hidden_estilo=estilo
            )

    return render_template("criar_personagem.html", etapa="inicial")

# ===== Listar personagens =====
@blueprint_personagem.route("/personagens")
def listar_personagens():
    personagens = carregar_personagens()
    return render_template("lista.html", personagens=personagens)
