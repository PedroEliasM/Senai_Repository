select
	pr.id_produto,
    pr.modelo,
    pr.preço,
    f.cd_fornecedor,
    e.id_estoque
from
	produto pr,
	fornecedor f,
    estoque e