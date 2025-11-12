from perfil import Perfil
from carreira import Carreira

def calcular_match(perfil: Perfil, carreira: Carreira) -> dict: # Calcula a pontuação de 'match' entre um perfil e uma carreira.
    pontuacao = 0
    competencias_match = []
    competencias_faltantes = []

    # Itera sobre os requisitos da carreira
    for req_comp, req_nivel in carreira.requisitos.items():
        # Verifica se o usuário tem a competência
        if req_comp in perfil.competencias:
            user_nivel = perfil.competencias[req_comp]
            # Se o usuário tem o nível, ganha pontos. Se supera, ganha bônus.
            if user_nivel >= req_nivel:
                pontuacao += (user_nivel - req_nivel) + 1 # Bônus
                competencias_match.append(f"{req_comp} (Seu nível: {user_nivel} / Requer: {req_nivel})")
            else:
                # Tem a skill mas o nível é baixo
                pontuacao -= (req_nivel - user_nivel)
                competencias_faltantes.append(f"{req_comp} (Seu nível: {user_nivel} / Requer: {req_nivel})")
        else:
            # Usuário não tem a competência
            pontuacao -= req_nivel
            competencias_faltantes.append(f"{req_comp} (Seu nível: 0 / Requer: {req_nivel})")

    # Retorna um dicionário (dict) com os resultados da análise
    return {
        "carreira": carreira.nome,
        "pontuacao": pontuacao,
        "match": competencias_match,
        "faltantes": competencias_faltantes
    }

def gerar_recomendacoes(perfil: Perfil, todas_carreiras: list[Carreira]) -> list[dict]: #  Compara o perfil com todas as carreiras e retorna uma lista ordenada.
    resultados = []
    for carreira in todas_carreiras:
        resultado_match = calcular_match(perfil, carreira)
        resultados.append(resultado_match)

    # Ordena a lista de resultados pela 'pontuacao', da maior para a menor
    resultados_ordenados = sorted(resultados, key=lambda r: r['pontuacao'], reverse=True)
    
    return resultados_ordenados