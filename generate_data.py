import random
import os
import psycopg2

students_names = [
    "Arthur Silva", "Bernardo Souza", "Caio Santos", "Daniel Oliveira", "Enzo Lima", "Felipe Pereira", "Gabriel Rodrigues",
    "Guilherme Gomes", "Henrique Costa", "Igor Vieira", "João Mendes", "Leonardo Cardoso", "Lucas Alves", "Marcelo Dias", 
    "Marcos Fernandes", "Mateus Marques", "Miguel Reis", "Nicolas Barros", "Pedro Freitas", "Rafael Lopes", "Vinicius Campos",
    "Ana Silva", "Beatriz Souza", "Bruna Santos", "Camila Oliveira", "Clara Lima", "Gabriela Pereira", "Isabella Rodrigues", 
    "Júlia Gomes", "Laís Costa", "Lara Vieira", "Laura Mendes", "Letícia Cardoso", "Lívia Alves", "Lorena Dias", 
    "Luana Fernandes", "Luiza Marques", "Manuela Reis", "Maria Barros", "Mariana Freitas", "Melissa Lopes", "Nicole Campos",
    "Arthur Silva", "Bernardo Souza", "Caio Santos", "Daniel Oliveira", "Enzo Lima", "Felipe Pereira", "Gabriel Rodrigues",
    "Guilherme Gomes", "Henrique Costa", "Igor Vieira", "João Mendes", "Leonardo Cardoso", "Lucas Alves", "Marcelo Dias", 
    "Marcos Fernandes", "Mateus Marques", "Miguel Reis", "Nicolas Barros", "Pedro Freitas", "Rafael Lopes", "Vinicius Campos",
    "Ana Silva", "Beatriz Souza", "Bruna Santos", "Camila Oliveira", "Clara Lima", "Gabriela Pereira", "Isabella Rodrigues", 
    "Júlia Gomes", "Laís Costa", "Lara Vieira", "Laura Mendes", "Letícia Cardoso", "Lívia Alves", "Lorena Dias", 
    "Luana Fernandes", "Luiza Marques", "Manuela Reis", "Maria Barros", "Mariana Freitas", "Melissa Lopes", "Nicole Campos",
    "Arthur Silva", "Bernardo Souza", "Caio Santos", "Daniel Oliveira", "Enzo Lima", "Felipe Pereira", "Gabriel Rodrigues",
    "Guilherme Gomes", "Henrique Costa", "Igor Vieira", "João Mendes", "Leonardo Cardoso", "Lucas Alves", "Marcelo Dias", 
    "Marcos Fernandes", "Mateus Marques", "Miguel Reis", "Nicolas Barros", "Pedro Freitas", "Rafael Lopes", "Vinicius Campos",
    "Ana Silva", "Beatriz Souza", "Bruna Santos", "Camila Oliveira", "Clara Lima", "Gabriela Pereira", "Isabella Rodrigues", 
    "Júlia Gomes", "Laís Costa", "Lara Vieira", "Laura Mendes", "Letícia Cardoso", "Lívia Alves", "Lorena Dias", 
    "Luana Fernandes", "Luiza Marques", "Manuela Reis", "Maria Barros", "Mariana Freitas", "Melissa Lopes", "Nicole Campos",
    "Arthur Silva", "Bernardo Souza", "Caio Santos", "Daniel Oliveira", "Enzo Lima", "Felipe Pereira", "Gabriel Rodrigues",
    "Guilherme Gomes", "Henrique Costa", "Igor Vieira", "João Mendes", "Leonardo Cardoso", "Lucas Alves", "Marcelo Dias", 
    "Marcos Fernandes", "Mateus Marques", "Miguel Reis", "Nicolas Barros", "Pedro Freitas", "Rafael Lopes", "Vinicius Campos",
    "Ana Silva", "Beatriz Souza", "Bruna Santos", "Camila Oliveira", "Clara Lima", "Gabriela Pereira", "Isabella Rodrigues", 
    "Júlia Gomes", "Laís Costa", "Lara Vieira", "Laura Mendes", "Letícia Cardoso", "Lívia Alves", "Lorena Dias", 
    "Luana Fernandes", "Luiza Marques", "Manuela Reis", "Maria Barros", "Mariana Freitas", "Melissa Lopes", "Nicole Campos",
    "Arthur Silva", "Bernardo Souza", "Caio Santos", "Daniel Oliveira", "Enzo Lima", "Felipe Pereira", "Gabriel Rodrigues",
    "Guilherme Gomes", "Henrique Costa", "Igor Vieira", "João Mendes", "Leonardo Cardoso", "Lucas Alves", "Marcelo Dias", 
    "Marcos Fernandes", "Mateus Marques", "Miguel Reis", "Nicolas Barros", "Pedro Freitas", "Rafael Lopes", "Vinicius Campos",
    "Ana Silva", "Beatriz Souza", "Bruna Santos", "Camila Oliveira", "Clara Lima", "Gabriela Pereira", "Isabella Rodrigues", 
    "Júlia Gomes", "Laís Costa", "Lara Vieira", "Laura Mendes", "Letícia Cardoso", "Lívia Alves", "Lorena Dias",]

def generate_id(n):
     id = ""
     for _ in range(n):
        id += random.choice("0123456789")
     return id

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
            
teachers_names = [
    "Ana Paula Silva", "Ana Carolina Souza", "Andréia Oliveira", "Beatriz Santos", "Bruna Lima", "Camila Pereira",
    "Carolina Rodrigues", "Cristiane Gomes", "Daniela Costa", "Edna Vieira", "Elaine Mendes", "Fabiana Cardoso",
    "Fernanda Alves", "Gabriela Dias", "Helena Fernandes", "Iara Marques", "Isabel Reis", "Jéssica Barros",
    "Joana Freitas", "Juliana Lopes", "Karina Campos", "Larissa Silva", "Leticia Souza", "Lorena Oliveira",
    "Luana Santos", "Luciana Lima", "Manuela Pereira", "Mariana Rodrigues", "Marina Gomes", "Marta Costa",
    "Matilde Vieira", "Mayara Mendes", "Melissa Cardoso", "Michele Alves", "Natalia Dias", "Pamela Fernandes",
    "Patricia Marques", "Paula Reis", "Rafaela Barros", "Raquel Freitas", "Regina Lopes", "Renata Campos",
    "Sabrina Silva", "Samantha Souza", "Sandra Oliveira", "Sarah Santos", "Sofia Lima", "Stella Pereira",
    "Suzana Rodrigues", "Tamara Gomes", "Vanessa Costa", "Veronica Vieira", "Vinicius Mendes", "Yuri Cardoso",
    "Alessandro Alves", "Bruno Dias", "Carlos Fernandes", "Daniel Marques", "Eduardo Reis", "Felipe Barros",
    "Fernando Freitas", "Gabriel Lopes", "Gustavo Campos", "Henrique Silva", "Igor Souza", "João Oliveira",
    "Jonathan Santos", "Leonardo Lima", "Lucas Pereira", "Marcelo Rodrigues", "Marcos Gomes", "Mateus Costa",
    "Maurício Vieira", "Miguel Mendes", "Nicolas Cardoso", "Pedro Alves", "Rafael Dias", "Renato Fernandes",
    "Ricardo Marques", "Roberto Reis", "Rodrigo Barros", "Samuel Freitas", "Thiago Lopes", "Tomas Campos",
    "Victor Silva", "Vinicius Souza", "Wagner Oliveira", "Walter Santos", "Wesley Lima", "William Pereira",
    "Xande Rodrigues", "Yuri Gomes", "Zeca Costa", "Ana Paula Silva", "Ana Carolina Souza", "Andréia Oliveira",
    "Beatriz Santos", "Bruna Lima", "Camila Pereira", "Carolina Rodrigues", "Cristiane Gomes", "Daniela Costa",
    "Edna Vieira", "Elaine Mendes", "Fabiana Cardoso", "Fernanda Alves", "Gabriela Dias", "Helena Fernandes",
    "Iara Marques", "Isabel Reis", "Jéssica Barros", "Joana Freitas", "Juliana Lopes", "Karina Campos",
    "Larissa Silva", "Leticia Souza", "Lorena Oliveira", "Luana Santos", "Luciana Lima", "Manuela Pereira",
    "Mariana Rodrigues", "Marina Gomes", "Marta Costa", "Matilde Vieira", "Mayara Mendes", "Melissa Cardoso",
    "Michele Alves", "Natalia Dias", "Pamela Fernandes", "Patricia Marques", "Paula Reis", "Rafaela Barros",
    "Raquel Freitas", "Regina Lopes", "Renata Campos", "Sabrina Silva", "Samantha Souza", "Sandra Oliveira",
    "Sarah Santos", "Sofia Lima", "Stella Pereira", "Suzana Rodrigues", "Tamara Gomes", "Vanessa Costa",
    "Veronica Vieira", "Vinicius Mendes", "Yuri Cardoso", "Alessandro Alves", "Bruno Dias", "Carlos Fernandes",
    "Daniel Marques", "Eduardo Reis", "Felipe Barros", "Fernando Freitas", "Gabriel Lopes", "Gustavo Campos",
    "Henrique Silva", "Igor Souza", "João Oliveira", "Jonathan Santos", "Leonardo Lima", "Lucas Pereira",
    "Marcelo Rodrigues", "Marcos Gomes", "Mateus Costa", "Maurício Vieira", "Miguel Mendes", "Nicolas Cardoso",
    "Pedro Alves", "Rafael Dias", "Renato Fernandes", "Ricardo Marques", "Roberto Reis", "Rodrigo Barros",
    "Samuel Freitas", "Thiago Lopes", "Tomas Campos", "Victor Silva", "Vinicius Souza", "Wagner Oliveira",
    "Walter Santos", "Wesley Lima", "William Pereira", "Xande Rodrigues", "Yuri Gomes", "Zeca Costa",
]

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

courses_names = [
    "Administração",
    "Arquitetura e Urbanismo",
    "Ciência da Computação",
    "Ciência de Dados",
    "Ciências Contábeis",
    "Comunicação Social",
    "Direito",
    "Educação Física",
    "Engenharia Civil",
    "Engenharia Elétrica",
    "Engenharia de Controle e Automação",
    "Engenharia de Robôs",
    "Engenharia Mecânica",
    "Engenharia Química",
    "Física",
    "História",
    "Jornalismo",
    "Matemática",
    "Medicina",
    "Pedagogia",
    "Psicologia",
    "Publicidade",
    "Serviço Social",
    "Tradução e Interpretação"
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

departments_names = [
    "Administração", "Ciência da Computação", "Ciências Contábeis", "Direito", "Engenharia", "Física",
    "Matemática", "Medicina", "Publicidade", "Química", "Direito"
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


subjects_names = [
    "Álgebra Linear",
    "Análise de Sistemas de Informação",
    "Arquitetura de Computadores",
    "Biologia Celular",
    "Cálculo Diferencial e Integral I",
    "Cálculo Diferencial e Integral II",
    "Cálculo Numérico",
    "Circuitos Elétricos I",
    "Circuitos Elétricos II",
    "Comunicação de Dados",
    "Contabilidade Geral",
    "Contabilidade de Custos",
    "Contabilidade Gerencial",
    "Dermatologia",
    "Direito Administrativo",
    "Direito Civil I",
    "Direito Civil II",
    "Direito Constitucional",
    "Direito Penal I",
    "Direito Penal II",
    "Direito do Trabalho",
    "Economia do Setor Público",
    "Eletromagnetismo",
    "Estatística Aplicada",
    "Ética Profissional",
    "Física Geral I",
    "Física Geral II",
    "Fisiologia Humana",
    "Fundamentos de Administração",
    "Fundamentos de Contabilidade",
    "Fundamentos de Direito",
    "Fundamentos de Economia",
    "Fundamentos de Estatística",
    "Fundamentos de Marketing",
    "Geometria Analítica",
    "História da Arte",
    "História do Brasil",
    "História do Direito",
    "Imunologia",
    "Inglês Instrumental",
    "Introdução à Administração",
    "Introdução à Contabilidade",
    "Introdução à Economia",
    "Introdução ao Direito",
    "Introdução à Estatística",
    "Introdução à Filosofia",
    "Introdução à Física",
    "Introdução à Matemática",
    "Introdução à Programação",
    "Introdução à Química",
    "Laboratório de Bioquímica",
    "Laboratório de Física I",
    "Laboratório de Física II",
    "Laboratório de Química Geral",
    "Língua Portuguesa",
    "Literatura Brasileira",
    "Logística",
    "Macroeconomia",
    "Matemática Discreta",
    "Matemática para Economistas",
    "Mecânica dos Sólidos",
    "Metodologia da Pesquisa",
    "Microeconomia",
    "Morfofisiologia Humana I",
    "Morfofisiologia Humana II",
    "Nutrição Humana",
    "Organização do Comportamento Humano nas Organizações",
    "Paradigmas da Administração",
    "Patologia Geral",
    "Política de Empresas",
    "Probabilidade e Estatística",
    "Psicologia Geral",
    "Química Geral",
    "Química Orgânica I",
    "Química Orgânica II",
    "Redes de Computadores",
    "Relações Internacionais",
    "Sistemas de Informação Gerenciais",
    "Sociologia Geral",
    "Teoria da Administração",
    "Teoria da Contabilidade",
    "Teoria do Direito",
    "Teoria Econômica",
    "Termodinâmica",
    "Topologia",
    "Toxicologia",
    "Técnicas de Apresentação e Comunicação",
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
        
def pg_connect(conn_str):
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    cur.execute("INSERT INTO professor (id, nome) VALUES (52142, 'Rodrigo Vales');")
    cur.close()
    return conn

def pg_fetch_one(conn, query_str):
    cursor = conn.cursor()
    cursor.execute(query_str)
    result = cursor.fetchone()
    cursor.close()
    return result

def pg_execute(conn, sql_str):
    cursor = conn.cursor()
    cursor.execute(sql_str)
    cursor.close()

pwd = "szyELkc5Arc7L-nsmGyKug"
pg_conn = pg_connect("postgresql://luiggi:szyELkc5Arc7L-nsmGyKug@luiggicluster-14355.7tt.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")