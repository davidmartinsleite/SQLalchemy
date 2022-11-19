from sqlalchemy import create_engine

motor = create_engine("mysql+pymysql://root:@localhost:3306/cadastro")
conexao = motor.connect()
resposta = conexao.execute('select * from gafanhotos;')

for fila in resposta:
    print(fila)
