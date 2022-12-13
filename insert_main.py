from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole
from models.revendedor import Revendedor
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole


# 1 Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a formula química: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
    with create_session() as session:
        session.add(an)
        session.commit()
    print(session)
    print('Aditivo Nutritivo cadastrado com sucesso')
    print(f'ID: {an.id}')
    print(f'NOME: {an.nome}')
    print(f'FORMULA QUÍMICA: {an.formula_quimica}')
    print(f'DATA: {an.data_criacao}')


# 2 Sabor
def insert_sabor() -> None:
    print('Cadastrando Sabor')

    nome: str = input('Informe o nome do Sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()
    print(session)
    print('Sabor cadastrado com sucesso')
    print(f'ID: {sabor.id}')
    print(f'NOME: {sabor.nome}')
    print(f'DATA: {sabor.data_criacao}')


# 3 Tipo Embalagem
def insert_tipo_embalagem() -> None:
    print('Cadastrando Tipo Embalagem')

    nome: str = input('Informe o nome do tipo de embalagem: ')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()
    print(session)
    print('Tipo de embalagem cadastrado com sucesso')
    print(f'ID: {tipo_embalagem.id}')
    print(f'NOME: {tipo_embalagem.nome}')
    print(f'DATA: {tipo_embalagem.data_criacao}')


# 4 Tipo Picole
def insert_tipo_picole() -> None:
    print('Cadastrando Tipo Picole')

    nome: str = input('Informe o nome do tipo de picole: ')

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()
    print(session)
    print('Tipo de picole cadastrado com sucesso')
    print(f'ID: {tipo_picole.id}')
    print(f'NOME: {tipo_picole.nome}')
    print(f'DATA: {tipo_picole.data_criacao}')


# 5 Ingrediente
def insert_ingrediente() -> None:
    print('Cadastrando Ingrediente')

    nome: str = input('Informe o nome do Ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()
    print(session)
    print('Ingrediente cadastrado com sucesso')
    print(f'ID: {ingrediente.id}')
    print(f'NOME: {ingrediente.nome}')
    print(f'DATA: {ingrediente.data_criacao}')


# 6 Conservante
def insert_conservante() -> None:
    print('Cadastrando Conservante')

    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()
    print(session)
    print('Conservante cadastrado com sucesso')
    print(f'ID: {conservante.id}')
    print(f'NOME: {conservante.nome}')
    print(f'DATA: {conservante.data_criacao}')


# 7 Revendedor
def insert_revendedor() -> None:
    print('Cadastrando Revendedor')

    cnpj: str = input('Informe o CNPJ do revendedor: ')
    razao_social: str = input('Informe a razão social do revendedor: ')
    contato: str = input('Informe o contato do revendedor: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()
    print(session)
    print('Revendedor cadastrado com sucesso')
    print(f'ID: {revendedor.id}')
    print(f'RAZÇAO SOCIAL: {revendedor.razao_social}')
    print(f'CNPJ: {revendedor.cnpj}')


# 8 Lote
def insert_lote() -> Lote:
    print('Cadastrando Lote')

    id_tipo_picole: str = input('Informe o ID do tipo de picolé: ')
    qnt: int = input('Digite a quantidade de picolé: ')

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=qnt)

    with create_session() as session:
        session.add(lote)
        session.commit()
    print(session)
    print('Lote cadastrado com sucesso')
    print(f'ID: {lote.id}')
    print(f'ID DO TIPO DE PICOLÉ: {lote.id_tipo_picole}')
    print(f'QUANTIDADE: {lote.quantidade}')
    return lote

    # 9 Nota Fiscal


def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastrando Nota Fiscal')

    valor: float = input('Informe o valor da nota fiscal: ')
    numero_serie: str = input('Informe o número série: ')
    descricao: str = input('Informe a descrição: ')
    id_revendedor: int = input('Informe o ID do revendedor: ')

    nota_fiscal: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao,
                                         id_revendedor=id_revendedor)

    with create_session() as session:
        session.add(nota_fiscal)
        session.commit()
    print(session)
    print('Nota fiscal cadastrada com sucesso')
    print(f'NUMERO SÉRIE: {nota_fiscal.numero_serie}')
    print(f'DESCRIÇÃO: {nota_fiscal.descricao}')
    print(f'ID DO REVENDEDOR: {nota_fiscal.id_revendedor}')

    return NotaFiscal

    # 10 Picole


def insert_picole() -> Picole:
    print('Cadastrando Picolé')

    preco: float = input('Informe o preco do picolé: ')
    id_sabor: int = input('Informe o ID do sabor: ')
    id_tipo_embalagem: int = input('Informe o ID do tipo de emabalagem: ')
    id_tipo_picole: int = input('Informe o ID do tipo de picole: ')

    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem,
                            id_tipo_picole=id_tipo_picole)
    with create_session() as session:
        session.add(picole)
        session.commit()
    print(session)
    print('Picolé cadastrado com sucesso')
    print(f'PREÇO: {picole.preco}')
    print(f'ID TIPO EMBALAGEM: {picole.id_tipo_embalagem}')
    print(f'ID DO SABOR: {picole.id_sabor}')

    return Picole


if __name__ == '__main__':
    insert_aditivo_nutritivo()
    insert_sabor()
    insert_tipo_embalagem()
    insert_tipo_picole()
    insert_ingrediente()
    insert_conservante()
    insert_revendedor()
    insert_lote()
    insert_nota_fiscal()
    insert_picole()
