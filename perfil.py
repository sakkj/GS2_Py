class Perfil: # Representa o perfil de um usuário com suas competências atuais.
    def __init__(self, nome: str):
        self.nome = nome
        # Chave = nome da competência / Valor = nível (1-5)
        self.competencias = {}

    def add_competencia(self, competencia: str, nivel: int): # Adiciona uma competência ao perfil do usuário.
        if nivel > 0 and nivel <= 5:
            self.competencias[competencia.lower()] = nivel
        else:
            print(f"Erro, nível para '{competencia}' deve estar entre 1 e 5.")

    def __str__(self): # Retorna uma representação em string do perfil.
        return f"Perfil de: {self.nome}"