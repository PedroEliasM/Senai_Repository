use loja_de_tenis;

create table produto(
	id_produto int auto_increment,
    modelo varchar(45) not null,
    categoria varchar(45) not null,
    tamanho int not null,
    cor varchar(30) not null,
    preço varchar(20) not null,
    cd_fornecedor int,
    
    constraint pk_produto primary key (id_produto),
    constraint fk_produto_fornecedor foreign key (cd_fornecedor) references fornecedor(cd_fornecedor)
)