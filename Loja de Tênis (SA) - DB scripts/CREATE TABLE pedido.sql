use loja_de_tenis;

create table pedido(
	id_pedido int auto_increment,
    status_pedido varchar(30) not null,
    dt_pedido date not null,
    valor_pedido varchar(16) not null,
	cd_cliente int,
    id_produto int,
    
    constraint pk_pedido primary key (id_pedido),
    constraint fk_pedido_cliente foreign key (cd_cliente) references cliente(cd_cliente),
    constraint fk_pedido_produto foreign key (id_produto) references produto(id_produto)
)