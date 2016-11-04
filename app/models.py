# -*- coding: utf8 -*-


def mostrarArray(array):
    aux = ""
    for a in array:
        aux = aux + str(a) + "\n"
    return aux


class Linguagem():
    def __init__(self, nome=None, tempo=None, frameworks=None):
        self.nome = nome
        self.tempo = tempo
        self.frameworks = []
        for f in frameworks:
            self.addFrameworks(f)

    def addFrameworks(self, framework):
        if framework not in self.frameworks:
            self.frameworks.append(framework)

    def mostrarFrameworks(self):
        aux = ""
        for f in self.frameworks:
            aux = aux + "    * " + str(f) + "\n"
        return aux

    def __str__(self):
        return (
            str(self.nome) + " - " + str(self.tempo) + "\n" +
            str(self.mostrarFrameworks())
        )


class Qualificacao():
    def __init__(self, resumo=None):
        self.resumo = resumo
        self.linguagens = []

    def addLinguagem(self, linguagem):
        if not isinstance(linguagem, Linguagem):
            raise ValueError(
                "A linguagem deve ser instancia de Linguagem."
            )
        if linguagem not in self.linguagens:
            self.linguagens.append(linguagem)

    def __str__(self):
        return (
            str(self.resumo) + "\n" +
            "Linguagens:\n" + mostrarArray(self.linguagens)
        )


class Experiencia():
    def __init__(self, data_inicio=None, data_fim=None,
                 empresa=None, cargo=None, atividades=None
                 ):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.empresa = empresa
        self.cargo = cargo
        self.atividades = atividades

    def __str__(self):
        return(
            "\n" +
            str(self.data_inicio) + " - " + str(self.data_fim) + " - " +
            str(self.empresa) + "\nCargo: " + str(self.cargo) + "\n" +
            "Atividades realizadas: " + str(self.atividades)
        )


class Formacao():
    def __init__(self, titulacao=None, local=None, semestre=None, status=None):
        self.titulacao = titulacao
        self.local = local
        self.semestre = semestre
        self.status = status

    def __str__(self):
        return (
            "\n" +
            str(self.titulacao) + "\n" +
            str(self.semestre) + "\n" +
            str(self.local) + "\n" +
            str(self.status)
        )


class Endereco():
    def __init__(self, estado=None, cidade=None,
                 bairro=None, rua=None, numero=None,
                 complemento=""):
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento

    def __str__(self):
        return (
            str(self.rua) + " Nº" + str(self.numero) + " " +
            str(self.complemento) + "\n" + str(self.bairro) + " - " +
            str(self.cidade) + " - " + str(self.estado)
        )


# Utilizado o "x" pela neutralidade de gênero
class Candidatx():
    def __init__(
        self, nome=None, idade=None, telefone=None,
        endereco=None, email=None, resumo=None,
        adicional=None, estado_civil=None
    ):
        self.nome = nome
        self.idade = idade
        self.estado_civil = estado_civil
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.resumo = resumo
        self.adicional = adicional
        self.experiencias = []
        self.formacoes = []

    def addQualificacao(self, qualificacao):
        if isinstance(qualificacao, Qualificacao):
            self.qualificacao = qualificacao
        else:
            raise ValueError(
                """A variável 'qualificacao' deve receber um objeto\
Qualificacao como parametro"""
            )

    def addExperiencia(self, experiencia):
        if isinstance(experiencia, Experiencia):
            self.experiencias.insert(0, experiencia)
        else:
            raise ValueError(
                """A variável experiencia deve receber um objeto Experiencia \
como parâmetro"""
            )

    def addFormacao(self, formacao):
        if isinstance(formacao, Formacao):
            self.formacoes.insert(0, formacao)
        else:
            raise ValueError(
                "A variável formação deve receber um objeto Formacao como parâmetro"
            )

    def mostrarCurriculo(self):
        return (
            str(self.nome) + "\n" +
            str(self.estado_civil) + ", " + str(self.idade) + " anos.\n" +
            str(self.endereco) + "\n" + "Telefone: " +
            str(self.telefone) + " / E-mail: " + str(self.email) + "\n" +
            "\nRESUMO\n" + str(self.resumo) + "\n" +
            "\nRESUMO DAS QUALIFICAÇÕES\n" + str(self.qualificacao) + "\n" +
            "\nFORMAÇÃO\n" + str(mostrarArray(self.formacoes)) + "\n" +
            "\nEXPERIÊNCIA PROFISSIONAL\n" +
            str(mostrarArray(self.experiencias)) + "\n" +
            "\nINFORMAÇÕES ADICIONAIS\n" + str(self.adicional)
        )

    def __str__(self):
        return str(self.nome)
