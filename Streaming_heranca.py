class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    @property
    def like(self):
        return self._like
    def dar_like(self):
        self._like += 1
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._like} likes'
    
class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._like} likes'
    
class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporada(s) - {self._like}'
    
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)
    
    
vingadores = Filmes('vingadores -ultimato', 2019, 160)
rsix = Series('round 6', 2021, 1)
megan = Filmes('m3gan', 2023, 90)
justiceiro = Series('justiceiro', 2018, 2)

filme_serie = [vingadores, rsix, megan, justiceiro]

playlist_sextou = Playlist('Filmes de sexta', filme_serie)

for programa in playlist_sextou.listagem:
    print(programa)