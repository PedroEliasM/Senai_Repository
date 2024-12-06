use loja_de_tenis;

create table cliente(
	cd_cliente int auto_increment,
	nome varchar(45) not null,
	email varchar(45) not null,
	telefone varchar(20) not null,
	endereço varchar(100) not null,
 
constraint pk_cliente primary key(cd_cliente)
)