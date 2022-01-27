from app import db


class Procedimentos:
    def __init__(self):
        self.identificador = []
        self.call_produtos_seller = "EXEC BuscadordeSeller @referenciadoseller = ident"
        self.call_sellers_google = "EXEC Buscadorconcorrente @nomeconcorrente = 'loja', @identseller = ident"
        self.call_produtos_sem_concorrente = "EXEC Buscaprodutossemconcorrentes @identseller = ident"
        self.call_menor_preco_concorrente = "EXEC Ordenamenorvalor @identseller = ident"
        self.call_maior_preco_concorrente ="EXEC Ordenamaiorvalor @identseller = ident"
        self.call_ganhando_preco = "EXEC GanhandoPreco @identseller = ident"
        self.call_perdendo_preco = "EXEC PerdendonoPreco @identseller = ident"
        
    def filtra_produtos_seller(self, idseller):
        proc = self.call_produtos_seller.replace("ident",idseller)
        executar = db.session.execute(proc).all()
        print(executar)
        return executar

    def filtrar_concorrentes_google(self, concorrente, idseller):
        proc = self.call_sellers_google.replace("loja",concorrente).replace("ident",idseller)
        executar = db.session.execute(proc).all()

    def filtrar_sem_concorrentes(self,idseller):
        proc = self.call_produtos_sem_concorrente.replace("ident",idseller)
        executar = db.session.execute(proc).all()
    
    def filtra_menor_valor_concorrencia(self, idseller):
        proc = self.call_menor_preco_concorrente.replace("ident",idseller)
        executar = db.session.execute(proc).all()

    
    def filtra_maior_valor_concorrencia(self, idseller):
        proc = self.call_maior_preco_concorrente.replace("ident",idseller)
        executar = db.session.execute(proc).all()

    def ganhando_preco_venda(self, idseller):
        proc = self.call_ganhando_preco.replace("ident",idseller)
        executar = db.session.execute(proc).all()

    
    def perdendo_preco_venda(self, idseller):
        proc = self.call_perdendo_preco.replace("ident",idseller)
        executar = db.session.execute(proc).all()






    



        
