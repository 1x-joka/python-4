# Implemente um exportador de dados funcuional para JSON e XML
# Aluno: + nome, + curso, + serie
    # JSON: + exportar()
    # XML: + exportar()
# Usuário: + nome, + email
    # JSON: + exportar()
    # XML: + exportar()

import json
import xml.etree.ElementTree as ET

class Aluno:

    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class JSONAluno(Aluno):

    def exportar(self):
        return json.dumps({
            'nome': self.nome,
            'curso': self.curso,
            'serie': self.serie
        }, ensure_ascii=False, indent=4)

class XMLAluno(Aluno):

    def exportar(self):
        aluno = ET.Element('aluno')

        ET.SubElement(aluno, 'nome').text = self.nome
        ET.SubElement(aluno, 'curso').text = self.curso
        ET.SubElement(aluno, 'serie').text = self.serie

        return ET.tostring(aluno, encoding='unicode')

class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class JSONUsuario(Usuario):

    def exportar(self):
        return json.dumps({
            'nome': self.nome,
            'email': self.email
        }, ensure_ascii=False, indent=4)


class XMLUsuario(Usuario):

    def exportar(self):
        usuario = ET.Element('usuario')

        ET.SubElement(usuario, 'nome').text = self.nome
        ET.SubElement(usuario, 'email').text = self.email

        return ET.tostring(usuario, encoding='unicode')

aluno_json = JSONAluno(
    'Joaquim',
    'Ciência de Dados',
    '3º ano'
)

aluno_xml = XMLAluno(
    'Joaquim',
    'Ciência de Dados',
    '3º ano'
)

usuario_json = JSONUsuario(
    'Joaquim',
    'joaquim@email.com'
)

usuario_xml = XMLUsuario(
    'Joaquim',
    'joaquim@email.com'
)


print('========== ALUNO JSON ==========')
print(aluno_json.exportar())

print('\n========== ALUNO XML ==========')
print(aluno_xml.exportar())

print('\n========== USUÁRIO JSON ==========')
print(usuario_json.exportar())

print('\n========== USUÁRIO XML ==========')
print(usuario_xml.exportar())