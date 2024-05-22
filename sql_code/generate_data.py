import random
from faker import Faker
fake = Faker('pt_BR')

def generate_id(n):
     id = ""
     for _ in range(n):
        id += "{}".format(random.randint(0, 9))
     return id
            

departments_names = [
    "Administração", "Ciência da Computação", "Engenharia", "Matemática", "Física"
]

departments = {}

for name in departments_names:
    id = generate_id(2)
    while id in departments:
        id = generate_id(2)
        if id not in departments:
            departments[id] = name
            break
    else:
        departments[id] = name


script = open("script.txt", "w")
for key, value in departments.items():
    script.write(f"INSERT INTO departamento (id, nome) VALUES ({int(key)}, '{value}');\n")

teachers_names = []
while len(teachers_names) < 50:
    complete_name = fake.name()
    teachers_names.append(complete_name)


teachers = {}
for name in teachers_names:
    id = generate_id(5)
    while id in teachers:
        id = generate_id(5)
        if id not in teachers:
            teachers[id] = name
            break
    else:
        teachers[id] = name

for id, nome in teachers.items():
    id_dept = random.sample(list(departments.keys()), 1)[0]
    script.write(f"INSERT INTO professor (id, nome, id_dept) VALUES ({int(id)}, '{nome}', {int(id_dept)});\n")

for id in departments.keys():
    id_prof = random.sample(list(teachers.keys()), 1)[0]
    str = f"UPDATE departamento SET chefe_dept = {int(id_prof)} WHERE id = {int(id)};\n"
    script.write(str)

courses_names = [
    "Administração",
    "Engenharia Civil",
    "Engenharia Elétrica",
    "Engenharia Mecânica",
    "Engenharia de Produção",
    "Engenharia Química",
    "Engenharia de Controle e Automação",
    "Engenharia de Computação",
    "Engenharia de Software",
    "Engenharia Ambiental",
    "Engenharia de Materiais",
    "Engenharia Naval",
    "Engenharia de Telecomunicações",
    "Engenharia Biomédica",
    "Engenharia de Petróleo",
    "Engenharia Aeroespacial",
    "Engenharia de Minas",
    "Engenharia Agronômica",
    "Ciência da Computação",
    "Sistemas de Informação",
    "Redes de Computadores",
    "Análise e Desenvolvimento de Sistemas",
    "Segurança da Informação",
    "Inteligência Artificial",
    "Big Data e Ciência de Dados",
    "Robótica",
    "Física",
    "Matemática"
]

courses = {}
for name in courses_names:
    id = generate_id(3)
    while id in courses:
        id = generate_id(3)
        if id not in courses:
            courses[id] = name
            break
    else:
        courses[id] = name

for id, nome in courses.items():
    id_dept = random.sample(list(departments.keys()), 1)[0]
    str = f"INSERT INTO curso (id, nome, id_dept) VALUES ({id}, '{nome}', {id_dept});\n"
    script.write(str) 

subjects_names = [
    "Cálculo Diferencial e Integral I",
    "Cálculo Diferencial e Integral II",
    "Álgebra Linear",
    "Geometria Analítica",
    "Física I",
    "Física II",
    "Química Geral",
    "Programação I",
    "Programação II",
    "Estruturas de Dados",
    "Algoritmos",
    "Banco de Dados",
    "Sistemas Operacionais",
    "Redes de Computadores",
    "Engenharia de Software I",
    "Engenharia de Software II",
    "Inteligência Artificial",
    "Aprendizado de Máquina",
    "Ciência de Dados",
    "Robótica",
    "Análise de Circuitos Elétricos",
    "Eletrônica Analógica",
    "Eletrônica Digital",
    "Sinais e Sistemas",
    "Controle de Sistemas",
    "Fundamentos de Engenharia de Controle",
    "Instrumentação",
    "Mecânica dos Sólidos",
    "Mecânica dos Fluidos",
    "Termodinâmica",
    "Resistência dos Materiais",
    "Materiais de Construção",
    "Gestão de Projetos",
    "Planejamento e Controle da Produção",
    "Logística",
    "Ergonomia",
    "Pesquisa Operacional",
    "Engenharia Econômica",
    "Probabilidade e Estatística",
    "Métodos Numéricos",
    "Hidráulica",
    "Geotecnia",
    "Transportes",
    "Análise Estrutural",
    "Construção Civil",
    "Gestão Ambiental",
    "Toxicologia Ambiental",
    "Recursos Hídricos",
    "Saneamento Básico",
    "Energia e Meio Ambiente",
    "Engenharia de Tráfego",
    "Pavimentação",
    "Estradas",
    "Pontes",
    "Telecomunicações",
    "Teoria Eletromagnética",
    "Processamento de Sinais",
    "Microprocessadores",
    "Sistemas Embarcados",
    "Engenharia de Software para Sistemas Embarcados",
    "Desenvolvimento de Jogos",
    "Computação Gráfica",
    "Realidade Virtual",
    "Big Data",
    "Mineração de Dados",
    "Segurança da Informação",
    "Criptografia",
    "Arquitetura de Computadores",
    "Compiladores",
    "Teoria da Computação",
    "Linguagens de Programação",
    "Interação Humano-Computador",
    "Empreendedorismo",
    "Inovação Tecnológica",
    "Projeto de Engenharia",
    "Simulação de Sistemas",
    "Engenharia de Requisitos",
    "Gestão da Qualidade",
    "Auditoria de Sistemas",
    "Planejamento Urbano",
    "Desenho Técnico",
    "Topografia",
    "Mecânica dos Solos",
    "Geologia de Engenharia",
    "Processos Industriais",
    "Bioengenharia",
    "Biomecânica",
    "Bioinformática",
    "Tecnologia de Alimentos",
    "Engenharia de Alimentos",
    "Processos Químicos",
    "Laboratório de Química",
    "Química Orgânica",
    "Química Inorgânica",
    "Termodinâmica Química",
    "Cálculo Numérico",
    "Matemática Discreta",
    "Teoria dos Grafos",
    "Redes Neurais",
    "Processamento de Imagens",
    "Sistemas Distribuídos",
    "Computação em Nuvem",
    "Internet das Coisas (IoT)",
    "Automação Industrial"
]

subjects = {}
for name in subjects_names:
    id = generate_id(8)
    while id in subjects:
        id = generate_id(8)
        if id not in subjects:
            subjects[id] = name
            break
    else:
        subjects[id] = name

for codigo, nome in subjects.items():
    id_dept = random.sample(list(departments.keys()), 1)[0]
    str = f"INSERT INTO disciplina (codigo, nome, id_dept) VALUES ({codigo}, '{nome}', {id_dept});\n"
    script.write(str)
    
students_names = []
while len(students_names) < 200:
    complete_name = fake.name()
    students_names.append(complete_name)

students = {}
for name in students_names:
    ra = generate_id(9)
    while ra in students:
        ra = generate_id(9)
        if ra not in students:
            students[ra] = name
            break
    else:
        students[ra] = name

for ra, nome in students.items():
    id_curso = random.sample(list(courses.keys()), 1)[0]
    str = f"INSERT INTO aluno (ra, nome, id_curso) VALUES ({ra}, '{nome}', {id_curso});\n"
    script.write(str)

semestre_matriz = 1
matriz_curricular = {}
for id_curso in courses.keys():
    for _ in range(5):
        id_subj = random.sample(list(subjects.keys()), 1)[0]
        matriz_curricular[semestre_matriz] = id_subj 
        str = f"INSERT INTO matriz_curricular (id_curso, id_disc, semestre) VALUES ({id_curso}, {id_subj}, {semestre_matriz});\n"
        script.write(str)
    semestre_matriz += 1

for id_aluno in students.keys():
    for _ in range(6):
        semester = random.sample(list(matriz_curricular.keys()), 1)[0]
        year = 0
        if (1 <= int(semester) <= 2): year = 2018
        if (3 <= int(semester) <= 4): year = 2019
        if (4 <= int(semester) <= 5): year = 2020
        if (5 <= int(semester) <= 6): year = 2021
        if (7 <= int(semester) <= 8): year = 2022
        if (8 <= int(semester) <= 9): year = 2023
        id_subj = random.sample(list(matriz_curricular.values()), 1)[0]
        point = random.randint(0, 10)
        str = f"INSERT INTO historico_escolar (id_aluno, cod_disc, semestre, ano, nota) VALUES ({id_aluno}, {id_subj}, {semester}, {year}, {point});\n"
        script.write(str)

for id_prof in teachers.keys():
    for _ in range(20):
        semester = random.randint(1, 9)
        year = random.randint(2000, 2024)
        id_subj = random.sample(list(subjects.keys()), 1)[0]
        str = f"INSERT INTO historico_disc_professor (id_prof, cod_disc, semestre, ano) VALUES ({id_prof}, {id_subj}, {semester}, {year});\n"
        script.write(str)
    
titulos_tcc = [
    "Análise de Estruturas de Concreto Armado em Edifícios Altos",
    "Desenvolvimento de Sistemas de Energia Solar Fotovoltaica em Áreas Urbanas",
    "Otimização de Processos de Produção em uma Indústria Automobilística",
    "Modelagem Computacional de Fluxo de Fluidos em Tubulações Industriais",
    "Impacto Ambiental da Indústria de Petróleo em Regiões Costeiras",
    "Automação de Processos Industriais com Uso de Controladores Lógicos Programáveis",
    "Desenvolvimento de Algoritmos para Reconhecimento de Padrões em Imagens Médicas",
    "Implementação de um Sistema de Gerenciamento de Banco de Dados para Empresas de Pequeno Porte",
    "Simulação de Tráfego Urbano Utilizando Redes Neurais Artificiais",
    "Análise da Viabilidade Econômica de Projetos de Energias Renováveis",
    "Desenvolvimento de um Software para Gestão de Projetos de Engenharia Civil",
    "Aplicação de Métodos de Controle Robusto em Sistemas de Automação Industrial",
    "Estudo de Materiais Alternativos para Construção Civil Sustentável",
    "Desenvolvimento de Aplicativos Móveis para Educação a Distância",
    "Segurança da Informação em Ambientes Corporativos: Desafios e Soluções",
    "Projeto de Redes de Computadores para Ambientes de Alta Disponibilidade",
    "Implementação de Algoritmos de Aprendizado de Máquina para Previsão de Demanda Energética",
    "Desenvolvimento de Jogos Educativos Utilizando Realidade Aumentada",
    "Análise de Sistemas de Comunicação Óptica em Redes Metropolitanas",
    "Desenvolvimento de Tecnologias Assistivas para Pessoas com Deficiência",
    "Estudo de Viabilidade Técnica e Econômica de Sistemas de Cogeração em Edifícios Comerciais",
    "Projeto e Implementação de Sistemas Embarcados para Monitoramento de Saúde",
    "Desenvolvimento de Algoritmos de Criptografia para Segurança em Redes sem Fio",
    "Otimização de Processos de Manufatura Aditiva em Impressoras 3D",
    "Desenvolvimento de Soluções de Big Data para Análise de Dados de Redes Sociais",
    "Estudo de Impacto Ambiental de Projetos de Infraestrutura de Transporte",
    "Desenvolvimento de Ferramentas de Análise de Desempenho para Redes de Computadores",
    "Aplicação de Técnicas de Inteligência Artificial em Sistemas de Diagnóstico Médico",
    "Desenvolvimento de Sistemas de Controle de Qualidade para a Indústria de Alimentos",
    "Projeto de Sistemas de Energia Eólica para Comunidades Rurais Isoladas",
    "Desenvolvimento de Algoritmos para Análise de Dados Genômicos",
    "Estudo da Dinâmica de Veículos Elétricos em Ambientes Urbanos",
    "Implementação de Sistemas de Monitoramento Ambiental Utilizando Redes de Sensores Sem Fio",
    "Análise de Viabilidade de Implantação de Sistemas de Irrigação Automatizados",
    "Desenvolvimento de Modelos Computacionais para Previsão de Desastres Naturais",
    "Projeto e Implementação de Sistemas de Telemetria para Veículos Autônomos",
    "Desenvolvimento de Algoritmos para Otimização de Redes de Distribuição de Energia",
    "Estudo de Soluções Tecnológicas para Tratamento de Água e Efluentes Industriais",
    "Aplicação de Métodos de Simulação Computacional em Projetos de Engenharia Aeroespacial",
    "Desenvolvimento de Sistemas de Automação para Edifícios Inteligentes",
    "Estudo da Utilização de Nanotecnologia em Processos de Purificação de Água",
    "Implementação de Sistemas de Detecção de Intrusos em Redes de Computadores",
    "Análise de Desempenho de Protocolos de Comunicação para Internet das Coisas (IoT)",
    "Desenvolvimento de Ferramentas de Visualização de Dados para Sistemas de Informação Geográfica",
    "Estudo de Técnicas de Bioinformática para Análise de Sequências de DNA",
    "Projeto de Sistemas de Controle de Tráfego Aéreo Utilizando Redes Neurais Artificiais",
    "Desenvolvimento de Soluções de Automação para a Indústria 4.0",
    "Análise de Sistemas de Energia Solar Térmica para Aquecimento de Água",
    "Estudo de Materiais Avançados para Aplicações em Engenharia Civil",
    "Implementação de Algoritmos de Processamento de Imagens para Detecção de Defeitos em Produtos Industriais",
    "Desenvolvimento de Modelos de Previsão de Demanda em Sistemas de Transporte Público",
    "Análise de Sistemas de Gestão de Resíduos Sólidos em Ambientes Urbanos",
    "Desenvolvimento de Sistemas de Comunicação para Redes de Sensores Submarinos",
    "Estudo de Técnicas de Mineração de Dados para Análise de Dados Educacionais",
    "Projeto de Sistemas de Controle para Veículos Autônomos de Transporte de Carga",
    "Desenvolvimento de Algoritmos para Reconhecimento de Voz em Aplicações Móveis",
    "Análise de Impacto Econômico de Projetos de Infraestrutura de Telecomunicações",
    "Desenvolvimento de Sistemas de Realidade Virtual para Treinamento de Profissionais de Saúde",
    "Estudo de Soluções Tecnológicas para Monitoramento de Mudanças Climáticas",
    "Projeto de Redes de Computadores para Ambientes Industriais",
    "Desenvolvimento de Algoritmos de Aprendizado Profundo para Análise de Imagens Médicas",
    "Estudo de Materiais Compósitos para Aplicações em Engenharia Mecânica",
    "Implementação de Sistemas de Automação para Processos de Manufatura",
    "Desenvolvimento de Tecnologias de Informação para Gestão de Recursos Hídricos",
    "Análise de Sistemas de Gestão de Energia em Edifícios Comerciais",
    "Desenvolvimento de Soluções de Segurança para Redes de Computadores Industriais",
    "Estudo de Técnicas de Inteligência Artificial para Previsão de Desempenho Escolar",
    "Projeto de Sistemas de Controle para Drones Utilizados em Agricultura de Precisão",
    "Desenvolvimento de Algoritmos para Análise de Dados de Sensores em Tempo Real",
    "Análise de Viabilidade de Implantação de Sistemas de Energia Solar em Residências",
    "Desenvolvimento de Sistemas de Informação para Gestão de Projetos de Construção Civil",
    "Estudo de Soluções de Automação para Processos de Produção de Alimentos",
    "Projeto de Sistemas de Comunicação para Veículos Autônomos",
    "Desenvolvimento de Algoritmos para Otimização de Rotas em Sistemas de Transporte",
    "Análise de Impacto Ambiental de Projetos de Infraestrutura Hidrelétrica",
    "Desenvolvimento de Sistemas de Monitoramento de Saúde para Idosos",
    "Estudo de Soluções Tecnológicas para Redução de Emissões de Gases de Efeito Estufa",
    "Projeto de Sistemas de Controle de Qualidade para a Indústria Farmacêutica",
    "Desenvolvimento de Ferramentas de Análise de Dados para Projetos de Engenharia",
    "Análise de Viabilidade de Implantação de Sistemas de Energia Eólica Offshore",
    "Desenvolvimento de Sistemas de Realidade Aumentada para Aplicações Industriais",
    "Estudo de Técnicas de Inteligência Artificial para Diagnóstico de Doenças",
    "Projeto de Redes de Computadores para Ambientes Acadêmicos",
    "Desenvolvimento de Algoritmos para Detecção de Anomalias em Redes de Computadores",
    "Análise de Sistemas de Gestão de Resíduos em Indústrias de Alimentos",
    "Desenvolvimento de Soluções de Big Data para Monitoramento Ambiental",
    "Estudo de Materiais Inteligentes para Aplicações em Engenharia Biomédica",
    "Implementação de Sistemas de Controle para Processos de Produção Sustentável",
    "Desenvolvimento de Tecnologias Assistivas para Pessoas com Deficiência Visual",
    "Análise de Impacto Econômico de Projetos de Energia Solar em Comunidades Rurais",
    "Desenvolvimento de Sistemas de Informação para Gestão de Saúde Pública",
    "Estudo de Técnicas de Mineração de Dados para Previsão de Comportamento do Consumidor",
    "Projeto de Sistemas de Automação para Processos de Manufatura de Produtos Eletrônicos",
    "Desenvolvimento de Algoritmos de Processamento de Sinais para Aplicações Biomédicas"
]
tcc = {}
for titulo in titulos_tcc:
    id = generate_id(3)
    while id in tcc:
        id = generate_id(3)
        if id not in tcc:
            tcc[id] = titulo
            break
    else:
        tcc[id] = titulo

x = 0
for id, name in tcc.items():
    id_prof = random.sample(list(teachers.keys()), 1)[0]
    str = f"INSERT INTO tcc (id, titulo, id_prof) VALUES ({id}, '{name}', {id_prof});\n"
    script.write(str)
    x += 1

for id in tcc.keys():
    id_aluno = random.sample(list(students.keys()), 4)
    for i in range(4):
        script.write(f"INSERT INTO grupo_tcc (id_tcc, id_aluno) VALUES ({id}, {id_aluno[i]});\n")