class Livro:
    def __init__(self,Nome,Autor,Editora,Paginas):
        self.nome = Nome
        self.autor = Autor
        self.editora = Editora
        self.paginas = Paginas

    def AlterarEditora(self,NovaEditora):
        self.editora = NovaEditora
        return f"Nova Editora: {self.editora}"
    
    def ListarQtdePaginas(self):
        return f"Quantidade de Páginas: {self.paginas}"
    
        
