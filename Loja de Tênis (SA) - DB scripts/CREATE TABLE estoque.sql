use loja_de_tenis;

create table estoque(
	id_estoque int not null,
    cd_fornecedor int,
	
	constraint pk_estoque primary key(id_estoque),
    constraint fk_estoque_fornecedor foreign key (cd_fornecedor) references fornecedor(cd_fornecedor)
)