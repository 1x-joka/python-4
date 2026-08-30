# Crie um simulador que gerencie a abertura de diferentes tipos de arquivos
# Arquivo (abstract): + nome, # _extensao, + tamanho, + @nome_completo, + abrir()
    # PDF
    # DOCX

from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome = '<desconhecido>', tamanho = 0):
        self.nome = nome
        self._extensao = ''
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        return f'{self.nome}{self._extensao}'
    
    @abstractmethod
    def abrir(self):
        pass

class PDF(Arquivo):
    def __init__(self, nome='<desconhecido>', tamanho=0):
        super().__init__(nome, tamanho)
        self._extensao = '.pdf'

    def abrir(self):
        print(f'Abrindo o arquivo PDF: {self.nome_completo}')

class DOCX(Arquivo):
    def __init__(self, nome='<desconhecido>', tamanho=0):
        super().__init__(nome, tamanho)
        self._extensao = '.docx'

    def abrir(self):
        print(f'Abrindo o arquivo DOCX: {self.nome_completo}')

arquivo_pdf = PDF('relatorio', 2500)
arquivo_docx = DOCX('curriculo', 1800)

print(f'Nome: {arquivo_pdf.nome}')
print(f'Tamanho: {arquivo_pdf.tamanho} KB')
print(f'Nome completo: {arquivo_pdf.nome_completo}')
arquivo_pdf.abrir()

print()

print(f'Nome: {arquivo_docx.nome}')
print(f'Tamanho: {arquivo_docx.tamanho} KB')
print(f'Nome completo: {arquivo_docx.nome_completo}')
arquivo_docx.abrir()