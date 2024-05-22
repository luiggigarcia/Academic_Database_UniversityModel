select a.nome as "aluno", h.cod_disc as "cod disc", d.nome as "disciplina",
h.semestre, h.ano, h.nota
from historico_escolar h
join aluno a
on a.ra = h.id_aluno 
join disciplina d
on d.codigo = h.cod_disc;

select p.nome as "professor", d.nome as "disciplina" ,h.semestre, h.ano
from professor p
join historico_disc_professor h
on p.id = h.id_prof
join disciplina d
on d.codigo = h.cod_disc;

select a.ra as "id_aluno", a.nome as "aluno"
from historico_escolar h
join matriz_curricular m
on m.id_disc = h.cod_disc and h.nota >= 5 and h.semestre = 4 and h.ano = 2020
join aluno a
on a.ra = h.id_aluno;

select p.nome as "chefe_dep", d.nome as "dept"
from departamento d
inner join professor p
on d.chefe_dept = p.id;

select t.id as "id_tcc", a.nome as "aluno", p.nome as "orientador"
from tcc t
join grupo_tcc g
on t.id = g.id_tcc
join aluno a 
on a.ra = g.id_aluno
join professor p
on p.id = t.id_prof;

