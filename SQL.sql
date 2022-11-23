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

CREATE TABLE IF NOT EXISTS atores (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    titulo_filme VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (titulo_filme) REFERENCES filmes(titulo)
);

INSERT INTO atores (nome, titulo_filme)
VALUE ("Tom Hanks", "Forest Gump");