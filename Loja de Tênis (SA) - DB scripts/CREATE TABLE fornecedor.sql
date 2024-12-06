use loja_de_tenis;

create table fornecedor(
	cd_fornecedor int auto_increment,
	nm_fornecedor varchar(20) not null,
    nm_produto varchar(30),
    
constraint pk_fornecedor primary key(cd_fornecedor)
)