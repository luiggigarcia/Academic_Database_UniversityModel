-- Historico escolar de todos os alunos.
select a.ra as "RA", a.nome as "aluno", h.cod_disc as "cod disc", d.nome as "disciplina",
h.semestre, h.ano, h.nota
from historico_escolar h
join aluno a
on a.ra = h.id_aluno 
join disciplina d
on d.codigo = h.cod_disc
order by semestre, a.nome;

-- Historico de disciplinas ministradas pelos professores.
select p.nome as "professor", d.nome as "disciplina" ,h.semestre, h.ano
from professor p
join historico_disc_professor h
on p.id = h.id_prof
join disciplina d
on d.codigo = h.cod_disc;

-- Todos os alunos que se formaram.
with alunos_formandos as (
	select distinct a.ra as "id_aluno", a.nome as "aluno", h.semestre, h.ano, d.nome as "disc", h.nota,
	h.nota >= 5 as "aprovado"
	from matriz_curricular m
	left join historico_escolar h
	on m.id_disc = h.cod_disc
	inner join aluno a
	on a.ra = h.id_aluno
	join disciplina d
	on d.codigo = h.cod_disc
	order by a.ra , h.ano, h.semestre
), formados as (
	select id_aluno, aluno, count(case when "aprovado" then 1 end) = count(disc) as "formado"
	from alunos_formandos
	group by id_aluno, aluno
)
select id_aluno, aluno, formado
from formados 
where formado;

-- Professores chefes de departamento e o nome do dept.
select p.nome as "chefe_dep", d.nome as "dept"
from departamento d
inner join professor p
on d.chefe_dept = p.id;

-- Alunos que fazem parte de um grupo de tcc e o seu orientador.
select t.id as "id_tcc", a.nome as "aluno", p.nome as "orientador"
from tcc t
join grupo_tcc g
on t.id = g.id_tcc
join aluno a 
on a.ra = g.id_aluno
join professor p
on p.id = t.id_prof
order by id_tcc;

