# -*- coding: utf8 -*-

from app import models

candidatx = models.Candidatx()

# Informações gerais
candidatx.nome = "Talita de Souza Rossari"
candidatx.idade = 18
candidatx.estado_civil = "Solteira"
candidatx.email = "rossaritalita@gmail.com"
candidatx.telefone = "(48) 9995-4764"
candidatx.endereco = models.Endereco(
    "Santa Catarina", "Florianópolis", "Ingleses",
    "Servidão Jatobá", "294", "AP01"
)

# Resumo
candidatx.resumo = "Técnica em Informatica pela instituição SENAI/SC. \n\
Graduanda em Analise e Desenvolvimento de Sistema pela instituição \
SENAI/SC. Com experiencia na área de Tecnologia da Informação, com ênfase \
em Desenvolvimento WEB.\n\
Co-organizadora das PyLadies Floripa."

# Qualificações
candidatx.addQualificacao(
    models.Qualificacao()
)

# Linguagens
candidatx.qualificacao.addLinguagem(
    models.Linguagem(
        "Java", "Três anos de experiência",
        ['Bibliotecas padrões', 'JSF', 'JPA', 'Hibernate']
    )
)
candidatx.qualificacao.addLinguagem(
    models.Linguagem(
        "SQL", "Três anos de experiência",
        ['MySQL', 'SQLServer', 'PostgreSQL', 'SQLite']
    )
)
candidatx.qualificacao.addLinguagem(
    models.Linguagem(
        "Python", "Um ano de experiência",
        ["Bibliotecas padrões", "Django", "Flask",
         "Tornado", """Pacote Data Science (Pandas, Matplotlib, Scipy, \
Numpy)"""]
    )
)
candidatx.qualificacao.addLinguagem(
    models.Linguagem(
        "JavaScript", "Dois anos de experiência",
        ["AngularJS", "JQuery", "Google Charts", "D3.js", "Ionic"]
    )
)
candidatx.qualificacao.addLinguagem(
    models.Linguagem(
        "R Language", "Um mês, ainda em pesquisa",
        ["Bibliotecas Padrões", "ggplot2"]
    )
)
candidatx.qualificacao.resumo = """Conhecimento de paradigma Orientado à Objetos, \
bancos de dados SQL, desenvolvimento web. Iniciando pesquisa no campo de Data Science."""

# Formação
candidatx.addFormacao(
    models.Formacao(
        "Superior de Tecnologia em Análise e Desenvolvimento de Sistemas",
        "Serviço Nacional de Aprendizagem Industrial - SENAI",
        "Terceiro Semestre", "Previsão de conclusão: 2018/1"
    )
)
candidatx.addFormacao(
    models.Formacao(
        "Técnico em Informatica - Programação",
        "Serviço Nacional de Aprendizagem Industrial - SENAI",
        "Concluído", "Concluído em 2015/1"
    )
)

# Experiencia
candidatx.addExperiencia(
    models.Experiencia(
        "01/09/2015", "Atual",
        "CIANET", "Estagiária Full Stack",
        """Desenvolvimento de serviços web com Django e Flask, e API RESTFUL \
com Tornado. Desenvolvimento de aplicativos mobile utilizando o Ionic. \
Conduzindo um estudo no campo de Data Science, utilizando Python, através do PyData \
e a linguagem R.  Conduzindo um estudo na área de BI e Data Analytics."""
    )
)
candidatx.addExperiencia(
    models.Experiencia(
        "04/03/2016", "Atual",
        "IFSC", "Pesquisadora e Desenvolvedora",
        """Pesquisa e desenvolvimento da plataforma WEB do projeto, utilizando \
o Framework Django. Otimizar rotinas através de scripts Python. Pesquisas no campo \
de Linked Data. Extração de dados públicos."""
    )
)
candidatx.addExperiencia(
    models.Experiencia(
        "18/06/2016", "23/07/2016",
        "IFSC", "Professora",
        """Ministrar aula básica de Python com foco em desenvolvimento WEB, \
utilizando o Framework Django."""
    )
)
candidatx.addExperiencia(
    models.Experiencia(
        "01/12/2014", "31/08/2015",
        "Serviço Nacional de Aprendizagem Industrial - SENAI",
        "Estagiária", """Desenvolvimento de recursos didáticos, produção dos \
cursos da modalidade à distância na plataforma SCORM, utilizando JavaScript nativo."""
    )
)

# Adiconal
candidatx.adicional = "Inglês intermediário"


if __name__ == "__main__":
    print(candidatx.mostrarCurriculo())
