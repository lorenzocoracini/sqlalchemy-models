from typing import List
from sqlalchemy import func
from conf.helpers import formata_data
from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor
from models.picole import Picole


# select simples
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # forma 1 (retorna objeto)
        # aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        # forma 2 (retorna lista)
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()

        for an in aditivos_nutritivos:
            print(f'ID:{an.id}')
            print(f'Data:{formata_data(an.data_criacao)}')
            print(f'Nome:{an.nome}')
            print(f'Formula Química:{an.formula_quimica}')


def select_filtro_sabor(id_sabor: int) -> Sabor:
    with create_session() as session:
        # forma 1 retorna None caso nao encontre
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()

        # forma 2 retorna None caso nao encontre
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        # forma 3 retorna exec.Notfound caso nao encontre
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()

        print(sabor.nome)
        print(f'Data:{formata_data(sabor.data_criacao)}')

        return sabor


# select complexo
def select_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()

        for p in picoles:
            print('-' * 30)
            print(f'ID: {p.id}')
            print(f'Data: {formata_data(p.data_criacao)}')
            print(f'Preço: {p.preco}')

            print(f'ID Sabor: {p.id_sabor}')
            print(f'Sabor: {p.sabor}')
            print(f'ID Embalagem: {p.id_tipo_embalagem}')
            print(f'Embalagem: {p.tipo_embalagem}')
            print(f'ID Tipo Picole: {p.id_tipo_picole}')
            print(f'Tipo picolé: {p.tipo_picole}')

            print(f'Ingredientes: {p.ingredientes}')
            print(f'Aditivos Nutritivos: {p.aditivos_nutritivos}')
            print(f'Conservantes: {p.conservantes}')


def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao).all()

        for s in sabores:
            print(f'ID: {s.id}')
            print(f'Nome: {s.nome}')


def select_group_by_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()

        for p in picoles:
            print('-' * 30)
            print(f'ID: {p.id}')
            print(f'Tipo Picolé: {p.tipo_picole.nome}')
            print(f'Sabor: {p.sabor.nome}')
            print(f'Preço: {p.preco}')


def select_limit() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(25)

        for s in sabores:
            print(f'ID: {s.id}')
            print(f'Nome: {s.nome}')


def select_count_revendedor() -> None:
    with create_session() as session:
        qtd: int = session.query(Revendedor).count()

        print(f'Quantidade: {qtd}')

def select_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro'),
        )

        print(f'A soma de todos os picolés é {resultado[0][0]}')
        print(f'A média de todos os picolés é {resultado[0][1]}')
        print(f'O valor mais barato de todos os picolés é {resultado[0][2]}')
        print(f'O valor mais caro de todos os picolés é {resultado[0][3]}')

if __name__ == '__main__':
    # select_todos_aditivos_nutritivos()
    # select_filtro_sabor(1)
    # select_picole()
    # select_order_by_sabor()
    # select_group_by_picole()
    # select_limit()
    # select_count_revendedor()
    select_agregacao()