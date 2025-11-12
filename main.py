import database
import engine
from perfil import Perfil


def criar_perfil_usuario() -> Perfil: # Função para criar o perfil do usuário via input.
    print("Criação de Perfil")
    nome = input("Digite seu nome: ")
    perfil_usuario = Perfil(nome)
    
    print("\nCadastre suas competências (Nível 1 a 5). Digite 'fim' para parar.")
    
    while True:
        competencia = input("Nome da competência (ex: lógica, python, colaboração): ")
        if competencia.lower() == 'fim':
            break
        
        try:
            nivel = int(input(f"Seu nível em '{competencia}' (1-5): "))
            if 1 <= nivel <= 5:
                perfil_usuario.add_competencia(competencia, nivel)
            else:
                print("Nível inválido. Deve ser entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
        
    print(f"\nPerfil de {nome} criado.")
    return perfil_usuario

def exibir_resultados(resultados: list[dict]): # Formata e exibe os resultados da recomendação.
    print("\nResultados da Análise")
    
    # Exibe as 3 melhores recomendações
    for i, res in enumerate(resultados[:3], 1):
        print(f"\nRecomendação número {i}: {res['carreira']} (Pontuação: {res['pontuacao']})")
        
        print("Pontos Fortes (Match):")
        if res['match']:
            for m in res['match']:
                print(f"{m}")
        else:
            print("Nenhuma competência em nível adequado")
        print()
        print("Áreas de Aprimoramento:")
        if res['faltantes']:
            for f in res['faltantes']:
                print(f"{f}")
        else:
            print("Nenhuma competência faltante!")

def main(): # Função Principal
    
    # 1. Carregar o "banco de dados" de carreiras
    todas_carreiras = database.get_carreiras()
    
    # 2. Criar o perfil do usuário
    perfil_usuario = criar_perfil_usuario()
    
    # 3. Rodar o motor de recomendação
    recomendacoes = engine.gerar_recomendacoes(perfil_usuario, todas_carreiras)
    
    # 4. Exibir os resultados
    exibir_resultados(recomendacoes)

# Ponto de entrada do script
if __name__ == "__main__":
    main()