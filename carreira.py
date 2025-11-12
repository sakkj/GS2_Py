class Carreira: # Representa uma carreira profissional com os requisitos de competência
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao
        # Chave = nome da competência / Valor = nível (1-5)
        self.requisitos = {}

    def add_requisito(self, competencia: str, nivel: int): # Adiciona um requisito de competência para esta carreira.
        if nivel > 0 and nivel <= 5:
            self.requisitos[competencia.lower()] = nivel
        else:
            print(f"Erro, nível para '{competencia}' deve estar entre 1 e 5.")

    def __str__(self): # Retorna uma representação em string da carreira.
        return f"Carreira: {self.nome}\nDescrição: {self.descricao}"