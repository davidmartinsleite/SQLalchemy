-- projeto SQLalchemy
create database cinema; -- cria o banco de dados

use cinema; -- acessa o banco de dados cadastro

create table filmes ( 
titulo varchar(50) not null, 
genero varchar(30) not null,
ano int not null,
primary key (titulo)
);

insert into filmes (titulo, genero, ano)
value ('Forest Gump', 'Drama', 1994);

describe filmes;

select * from filmes;

