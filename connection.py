from sqlalchemy import create_engine

motor = create_engine("mysql+pymysql://root:@localhost:3306/cinema")
conexao = motor.connect()
resposta = conexao.execute('select * from filmes;')

for fila in resposta:
    print(fila)

