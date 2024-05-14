create table departamento (
	id int,
	nome varchar,
	chefe_dept int,
	primary key (id),
	foreign key (chefe_dept) references professor(id)
);

create table professor (
	id int,
	nome varchar(255),
	id_dept int,
	primary key (id),
	foreign key (id_dept) references departamento(id)
);

create table curso (
	id int,
	nome varchar,
	id_dept int,
	primary key (id),
	foreign key (id_dept) references departamento(id)
);

create table disciplina ( 
	codigo varchar,
	nome varchar,
	id_dept int,
	primary key (codigo),
	foreign key (id_dept) references departamento(id)
);

create table matriz_curricular ( 
	id int,
	id_curso int,
	id_disc varchar,
	semestre int
	primary key (id),
	foreign key (id_curso) references curso(id),
	foreign key (id_disc) references disciplina(codigo)
);

create table aluno (  
	ra varchar,
	nome varchar,
	id_curso int,
	primary key (ra),
	foreign key (id_curso) references curso(id)
);

create table historico_escolar ( 
	id int,
	id_aluno varchar,
	id_disc varchar,
	semestre int,
	ano int,
	nota numeric
	primary key (id),
	foreign key (id_aluno) references aluno(ra),
	foreign key (id_disc) references disciplina(codigo)
);

create table historico_disc_professor (
	id int,
	id_prof int,
	cod_disc varchar,
	semestre int,
	ano int,
	primary key (id),
	foreign key (id_prof) references professor(id),
	foreign key cod_disc references disciplina(codigo)
);


create table tcc (
	id int,
	titulo varchar,
	id_prof int,
	primary key (id),
	foreign key (id_prof) references professor(id)
);

create table grupo_tcc (
	id int,
	id_tcc int,
	id_aluno varchar,
	primary key (id),
	foreign key (id_tcc) references tcc(id),
	foreign key (id_aluno) references aluno(ra)
);





















