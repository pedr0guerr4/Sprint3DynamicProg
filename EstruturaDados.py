import pandas as pd

residentes = {
    'residente_1': {'nome': 'Dr. João', 'progresso': []},
    'residente_2': {'nome': 'Dra. Ana', 'progresso': []},
    'residente_3': {'nome': 'Dr. Carlos', 'progresso': []}
}

resultados_intermediarios = [
    {'id_sessao': 1, 'residente': 'residente_1', 'desempenho': 85, 'erros': 3},
    {'id_sessao': 2, 'residente': 'residente_2', 'desempenho': 90, 'erros': 2}
]

df_resultados = pd.DataFrame(resultados_intermediarios)

def registrar_treinamento(residente_id, desempenho, erros):
    if residente_id not in residentes:
        return f"Erro: Residente '{residente_id}' não encontrado."

    nova_sessao = {
        'id_sessao': len(resultados_intermediarios) + 1,
        'residente': residente_id,
        'desempenho': desempenho,
        'erros': erros
    }

    residentes[residente_id]['progresso'].append(nova_sessao['id_sessao'])

    resultados_intermediarios.append(nova_sessao)
    df_resultados_atualizado = pd.DataFrame(resultados_intermediarios)
    return df_resultados_atualizado


def fornecer_feedback(desempenho, erros):
    if desempenho >= 90:
        feedback = "Excelente! Continue assim."
    elif desempenho >= 75:
        feedback = "Bom desempenho, mas há espaço para melhorias. Atenção aos erros."
    else:
        feedback = "Desempenho abaixo do esperado. Recomenda-se prática adicional."

    if erros > 5:
        feedback += " Muitos erros cometidos, recomenda-se revisar a técnica."

    return feedback


df_atualizado = registrar_treinamento('residente_3', 78, 4)
feedback = fornecer_feedback(78, 4)

print(df_atualizado)
print(feedback)
