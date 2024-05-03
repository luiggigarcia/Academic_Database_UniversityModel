-- DDL
create table departamento (
    id int not null,
    nome varchar not null,
    chefe_dept varchar,
    primary key (id)
)

create table curso (
    id int not null,
    nome varchar not null,
    id_dept int not null,
    primary key (id),
    foreign key (id_dept) references departamento(id)
)

create table disciplina (
    codigo varchar not null,
    nome varchar not null,
    id_dept int not null,
    primary key (codigo),
    foreign key (id_dept) references departamento(id)
)

create matriz_curricular (
    id_curso int not null,
    id_disciplina varchar not null,
    id_dept int not null,
    foreign key (id_curso) references curso(id),
    foreign key (id_disciplina) references disciplina(codigo),
    foreign key (id_dept) references departamento(id)
)

create table aluno (
    ra varchar not null,
    nome varchar not null,
    id_curso int not null,
    foreign key (id_curso) references curso(id),
    primary key (ra)
    ) 

create table professor (
    id int not null,
    nome varchar not null,
    id_dept int not null
    primary key (id)
    foreign key (id_dept) references departamento(id)
)
