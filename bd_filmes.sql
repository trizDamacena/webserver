create database bd_filmes;
use bd_filmes;

create table filme(
	id int primary key auto_increment,
    titulo varchar(255) not null,
    orcamento double not null,
    tempo_duracao varchar(10) not null,
    ano int not null,
    poster varchar(255) not null
);

create table diretor(
	id int primary key auto_increment,
    nome varchar(50) not null,
    sobrenome varchar(150) not null,
    genero varchar(60) not null,
    nacionalidade varchar(250) not null
);

create table atores(
	id int primary key auto_increment,
    nome varchar(100) not null,
    sobrenome varchar(150) not null,
    genero varchar(25) not null,
    nacionalidade varchar(100) not null
);

create table linguagem(
	id int primary key auto_increment,
    linguagem varchar(60) not null
);

create table pais(
	id int primary key auto_increment,
    pais varchar(60) not null
);

create table produtora(
	id int primary key auto_increment,
    produtora varchar(100) not null
);

create table genero(
	id int primary key auto_increment,
    genero varchar(60) not null
);

create table diretor_filmes(
	id int primary key auto_increment,
    diretor_id int not null,
    filmes_id int not null,
    
    foreign key(diretor_id) references diretor(id),
    foreign key(filmes_id) references filme(id)
);

create table atores_filmes(
	id int primary key auto_increment,
    atores_id int not null,
    filmes_id int not null,

    foreign key(atores_id) references atores(id),
    foreign key(filmes_id) references filme(id)
);

create table genero_filme(
	id int primary key auto_increment,
    genero_id int not null,
    filme_id int not null,
    
    foreign key(genero_id) references genero(id),
    foreign key(filme_id) references filme(id)
);

create table produtora_filme(
	id int primary key auto_increment,
    produtora_id int not null,
    filme_id int not null,
    
    foreign key(produtora_id) references produtora(id),
    foreign key(filme_id) references filme(id)
);

create table pais_filmes(
	id int primary key auto_increment,
    pais_id int not null,
    filme_id int not null,
    
    foreign key(pais_id) references pais(id),
    foreign key(filme_id) references filme(id)
);

create table linguagem_filme(
	id int primary key auto_increment,
    linguagem_id int not null,
    filme_id int not null,
    
    foreign key(linguagem_id) references linguagem(id),
    foreign key(filme_id) references filme(id)
);

INSERT INTO filme(titulo, orcamento, tempo_duracao, ano, poster)
VALUES
("Duro de matar", "28", "02:12:00", "1988", "https://br.web.img2.acsta.net/medias/nmedia/18/92/25/88/20188922.jpg"),
("O Poderoso Chefão", "6", "02:55:00", "1972", "https://br.web.img3.acsta.net/r_1280_720/pictures/19/04/09/15/42/3376326.jpg"),
("Forrest Gump", "55", "02:22:00", "1994", "https://uauposters.com.br/media/catalog/product/3/5/352820210407-uau-posters-forrest-gump-filmes-3.jpg"),
("Gladiador", "103", "02:35:00", "2000", "https://br.web.img2.acsta.net/medias/nmedia/18/91/24/64/20145017.jpg"),
("Interestelar", "165", "02:49:00", "2014", "https://br.web.img2.acsta.net/pictures/14/10/01/20/59/326428.jpg"),
("A Origem", "160", "02:28:00", "2010", "https://br.web.img3.acsta.net/medias/nmedia/18/78/91/50/19782909.jpg"),
("Os Vingadores", "220", "02:23:00", "2012", "https://br.web.img3.acsta.net/medias/nmedia/18/90/15/42/20106611.jpg"),
("Titanic", "200", "03:14:00", "1997", "https://br.web.img2.acsta.net/medias/nmedia/18/87/95/69/19873983.jpg"),
("Clube da Luta", "63", "02:19:00", "1999", "https://br.web.img3.acsta.net/medias/nmedia/18/91/96/58/20150641.jpg"),
("Matrix", "63", "02:16:00", "1999", "https://br.web.img3.acsta.net/medias/nmedia/18/95/05/76/20496215.jpg"),
("O Senhor dos Anéis: A Sociedade do Anel", "93", "02:58:00", "2001", "https://br.web.img2.acsta.net/medias/nmedia/18/91/96/60/20150659.jpg"),
("Pulp Fiction", "8", "02:34:00", "1994", "https://br.web.img2.acsta.net/medias/nmedia/18/91/00/86/20141351.jpg"),
("O Cavaleiro das Trevas", "185", "02:32:00", "2008", "https://br.web.img3.acsta.net/medias/nmedia/18/90/68/47/20112216.jpg"),
("Jogos Vorazes", "78", "02:22:00", "2012", "https://br.web.img2.acsta.net/medias/nmedia/18/87/01/59/20028611.jpg"),
("Velozes e Furiosos", "38", "01:46:00", "2001", "https://br.web.img2.acsta.net/medias/nmedia/18/91/04/57/20128742.jpg"),
("O Lobo de Wall Street", "100", "03:00:00", "2013", "https://br.web.img2.acsta.net/medias/nmedia/18/92/96/10/20304006.jpg"),
("Coringa", "55", "02:02:00", "2019", "https://br.web.img3.acsta.net/pictures/19/08/26/20/23/3792184.jpg"),
("O Rei Leão", "45", "01:29:00", "1994", "https://br.web.img3.acsta.net/medias/nmedia/18/87/35/61/19873674.jpg"),
("Harry Potter e a Pedra Filosofal", "125", "02:32:00", "2001", "https://br.web.img2.acsta.net/medias/nmedia/18/90/95/35/20106184.jpg"),
("Avatar", "237", "02:42:00", "2009", "https://br.web.img2.acsta.net/medias/nmedia/18/87/90/79/19874055.jpg");


insert into diretor(nome, sobrenome, genero, nacionalidade)
values
("John", "McTiernan", "Masculino", "Americano"),
("Francis", "Coppola", "Masculino", "Americano"),
("Robert", "Zemeckis", "Masculino", "Americano"),
("Ridley", "Scott", "Masculino", "Britânico"),
("Christopher", "Nolan", "Masculino", "Britânico"),
("Christopher", "Nolan", "Masculino", "Britânico"),
("Joss", "Whedon", "Masculino", "Americano"),
("James", "Cameron", "Masculino", "Canadense"),
("David", "Fincher", "Masculino", "Americano"),
("Lana", "Wachowski", "Feminino", "Americana"),
("Peter", "Jackson", "Masculino", "Neozelandês"),
("Quentin", "Tarantino", "Masculino", "Americano"),
("Christopher", "Nolan", "Masculino", "Britânico"),
("Gary", "Ross", "Masculino", "Americano"),
("Rob", "Cohen", "Masculino", "Americano"),
("Martin", "Scorsese", "Masculino", "Americano"),
("Todd", "Phillips", "Masculino", "Americano"),
("Roger", "Allers", "Masculino", "Americano"),
("Chris", "Columbus", "Masculino", "Americano"),
("James", "Cameron", "Masculino", "Canadense");

INSERT INTO atores(nome, sobrenome, genero, nacionalidade)
VALUES
("Bruce", "Willis", "Masculino", "Americano"),
("Marlon", "Brando", "Masculino", "Americano"),
("Tom", "Hanks", "Masculino", "Americano"),
("Russell", "Crowe", "Masculino", "Neozelandês"),
("Matthew", "McConaughey", "Masculino", "Americano"),
("Leonardo", "DiCaprio", "Masculino", "Americano"),
("Robert", "Downey Jr.", "Masculino", "Americano"),
("Kate", "Winslet", "Feminino", "Britânica"),
("Brad", "Pitt", "Masculino", "Americano"),
("Keanu", "Reeves", "Masculino", "Canadense"),
("Elijah", "Wood", "Masculino", "Americano"),
("Uma", "Thurman", "Feminino", "Americana"),
("Heath", "Ledger", "Masculino", "Australiano"),
("Jennifer", "Lawrence", "Feminino", "Americana"),
("Paul", "Walker", "Masculino", "Americano"),
("Leonardo", "DiCaprio", "Masculino", "Americano"),
("Joaquin", "Phoenix", "Masculino", "Americano"),
("Matthew", "Broderick", "Masculino", "Americano"),
("Daniel", "Radcliffe", "Masculino", "Britânico"),
("Sam", "Worthington", "Masculino", "Australiano");

INSERT INTO linguagem(linguagem)
VALUES
("Inglês"),
("Português"),
("Espanhol"),
("Francês"),
("Alemão"),
("Italiano"),
("Japonês"),
("Coreano"),
("Chinês Mandarim"),
("Russo"),
("Árabe"),
("Hindi"),
("Turco"),
("Grego"),
("Sueco"),
("Norueguês"),
("Holandês"),
("Polonês"),
("Tailandês"),
("Hebraico");

INSERT INTO pais(pais)
VALUES
("Estados Unidos"),
("Brasil"),
("Reino Unido"),
("França"),
("Alemanha"),
("Itália"),
("Canadá"),
("Austrália"),
("Nova Zelândia"),
("Espanha"),
("Japão"),
("Coreia do Sul"),
("China"),
("Índia"),
("México"),
("Argentina"),
("Suécia"),
("Noruega"),
("Rússia"),
("África do Sul");

INSERT INTO produtora(produtora)
VALUES
("20th Century Fox"),
("Paramount Pictures"),
("DreamWorks Pictures"),
("Legendary Pictures"),
("Warner Bros."),
("Marvel Studios"),
("New Line Cinema"),
("Miramax Films"),
("Lionsgate"),
("Universal Pictures"),
("Walt Disney Pictures");

INSERT INTO genero(genero)
VALUES
("Ação"),
("Drama"),
("Ficção Científica"),
("Suspense"),
("Aventura"),
("Romance"),
("Crime"),
("Comédia"),
("Fantasia"),
("Animação"),
("Super-herói"),
("Guerra"),
("Terror"),
("Mistério"),
("Biografia"),
("Histórico"),
("Musical"),
("Família"),
("Thriller Psicológico"),
("Épico");

INSERT INTO diretor_filmes(diretor_id, filmes_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20);

INSERT INTO atores_filmes(atores_id, filmes_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20);

INSERT INTO genero_filme(genero_id, filme_id)
VALUES
(1, 1),   -- Duro de Matar - Ação
(2, 2),   -- O Poderoso Chefão - Drama
(2, 3),   -- Forrest Gump - Drama
(1, 4),   -- Gladiador - Ação
(3, 5),   -- Interestelar - Ficção Científica
(1, 6),   -- A Origem - Ação
(11, 7),  -- Os Vingadores - Super-herói
(6, 8),   -- Titanic - Romance
(2, 9),   -- Clube da Luta - Drama
(3, 10),  -- Matrix - Ficção Científica
(5, 11),  -- Senhor dos Anéis - Aventura
(7, 12),  -- Pulp Fiction - Crime
(11, 13), -- Cavaleiro das Trevas - Super-herói
(5, 14),  -- Jogos Vorazes - Aventura
(1, 15),  -- Velozes e Furiosos - Ação
(15, 16), -- Lobo de Wall Street - Biografia
(19, 17), -- Coringa - Thriller Psicológico
(10, 18), -- O Rei Leão - Animação
(9, 19),  -- Harry Potter - Fantasia
(3, 20);  -- Avatar - Ficção Científica

INSERT INTO produtora_filme(produtora_id, filme_id)
VALUES
(1, 1),
(2, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(1, 8),
(1, 9),
(5, 10),
(7, 11),
(8, 12),
(5, 13),
(9, 14),
(10, 15),
(2, 16),
(5, 17),
(11, 18),
(5, 19),
(1, 20);

INSERT INTO pais_filmes(pais_id, filme_id)
VALUES
(1, 1),
(1, 2),
(1, 3),
(3, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(3, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(1, 18),
(3, 19),
(1, 20);

INSERT INTO linguagem_filme(linguagem_id, filme_id)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(1, 18),
(1, 19),
(1, 20);

select * from filme;
select * from diretor;
select * from atores;
select * from linguagem;
select * from pais;
select * from produtora;
select * from genero;
select * from diretor_filmes;
select * from atores_filmes;
select * from genero_filme;
select * from produtora_filme;
select * from pais_filmes;
select * from linguagem_filme;


drop database bd_filmes;

