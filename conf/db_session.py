import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from typing import Optional
from sqlalchemy.future.engine import Engine
from models.model_base import ModelBase
import models.__all_models

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    # função para configurar a conexão com o banco de dados

    global __engine

    if __engine:
        return

    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={'check_same_thread': False})


    # postgree
    else:
        conn_str = 'postgresql://postgres:Inter1909.@localhost:5432/picoles'
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    # função para criar a sessão de conexão ao banco de dados

    global __engine

    if not __engine:
        create_engine()  # se for sqlite (sqlite=True)

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables():
    global __engine

    if not __engine:
        create_engine()  # se for sqlite (sqlite=True)

    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
