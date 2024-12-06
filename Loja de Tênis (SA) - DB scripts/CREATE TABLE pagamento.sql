use loja_de_tenis;

create table pagamento(
	cd_pagamento int not null auto_increment,
	dt_pagamento date not null,
	forma_pagamento varchar(45) not null,
    id_pedido int,

	constraint pk_pagamento primary key(cd_pagamento),
    constraint fk_pagamento_pedido foreign key (id_pedido) references pedido(id_pedido)
)