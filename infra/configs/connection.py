from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__conection_string = "mysql+pymysql://root:@localhost:3306/cinema"  # essa é a string de conexão
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):  # metodo privado para criar uma engine
        engine = create_engine(self.__conection_string)
        return engine

    def get_engine(self):
        return self.__engine

    # nesse metodo com o 'enter' e 'exit' vamos poder abrir a cessão e fecha-la sem
    # problemas agora, essa estrutura da exemplifica no arquivo 'metodo with (enter, exit)'
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
