from carreira import Carreira

def get_carreiras() -> list[Carreira]: # Cria e retorna uma lista de todas as carreiras disponíveis no sistema.
    lista_carreiras = []

    # Carreira 1: Cientista de Dados (cd)
    cd = Carreira("Cientista de Dados", "Analisa grandes volumes de dados para extrair insights.")
    cd.add_requisito("lógica", 5)
    cd.add_requisito("python", 4)
    cd.add_requisito("estatística", 5)
    cd.add_requisito("colaboração", 3)
    lista_carreiras.append(cd)

    # Carreira 2: Designer UX/UI (ux)
    ux = Carreira("Designer UX/UI", "Projeta a experiência e interface do usuário em produtos digitais.")
    ux.add_requisito("criatividade", 5)
    ux.add_requisito("empatia", 4)
    ux.add_requisito("colaboração", 4)
    ux.add_requisito("lógica", 2)
    lista_carreiras.append(ux)
    
    # Carreira 3: Gerente de Projetos (gp)
    gp = Carreira("Gerente de Projetos", "Organiza e lidera equipes em um projeto.")
    gp.add_requisito("colaboração", 5)
    gp.add_requisito("liderança", 5)
    gp.add_requisito("comunicação", 4)
    gp.add_requisito("lógica", 3)
    lista_carreiras.append(gp)

    # Pode-se adicionar mais carreiras por aqui...

    return lista_carreiras