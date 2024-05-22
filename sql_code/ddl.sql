drop table departamento, professor, curso, disciplina, matriz_curricular, aluno, historico_escolar,
historico_disc_professor, tcc, grupo_tcc;

create table departamento (
	id int,
	nome varchar,
	chefe_dept int,
	primary key (id)
);

create table professor (
	id int,
	nome varchar(255),
	id_dept int,
	primary key (id)
);

alter table departamento
add foreign key (chefe_dept) references professor(id) 
on delete cascade;

alter table professor
add foreign key (id_dept) references departamento(id)
on delete cascade;

create table curso (
	id int,
	nome varchar,
	id_dept int,
	primary key (id),
	foreign key (id_dept) references departamento(id)
	on delete set null
);

create table disciplina ( 
	codigo int,
	nome varchar,
	id_dept int,
	primary key (codigo),
	foreign key (id_dept) references departamento(id)
	on delete set null
);

create table matriz_curricular ( 
	id serial,
	id_curso int,
	id_disc int,
	semestre int,
	primary key (id),
	foreign key (id_curso) references curso(id)
	on delete cascade,
	foreign key (id_disc) references disciplina(codigo)
	on delete cascade
);

create table aluno (  
	ra varchar,
	nome varchar,
	id_curso int,
	primary key (ra),
	foreign key (id_curso) references curso(id)
	on delete cascade
);

create table historico_escolar ( 
	id serial,
	id_aluno varchar,
	cod_disc int,
	semestre int,
	ano int,
	nota numeric,
	primary key (id),
	foreign key (id_aluno) references aluno(ra)
	on delete cascade,
	foreign key (cod_disc) references disciplina(codigo)
	on delete cascade
);

create table historico_disc_professor (
	id serial,
	id_prof int,
	cod_disc int,
	semestre int,
	ano int,
	primary key (id),
	foreign key (id_prof) references professor(id)
	on delete cascade,
	foreign key (cod_disc) references disciplina(codigo)
	on delete cascade
);


create table tcc (
	id int,
	titulo varchar,
	id_prof int,
	primary key (id),
	foreign key (id_prof) references professor(id)
	on delete set null
);

create table grupo_tcc (
	id serial,
	id_tcc int,
	id_aluno varchar,
	primary key (id),
	foreign key (id_tcc) references tcc(id)
	on delete cascade,
	foreign key (id_aluno) references aluno(ra)
	on delete cascade
);





















