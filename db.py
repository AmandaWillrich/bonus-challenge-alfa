import psycopg2


class ConnectDb:

    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='password123'
        )

    def update_or_create_company(self, company):
        cursor = self.connection.cursor()
        sql = f"""
            INSERT INTO FILIAIS_ALFA
            VALUES (
                DEFAULT,
                '{company.cnpj}',
                '{company.nome}',
                '{company.cidade}',
                '{company.estado}'
            )
            ON CONFLICT (cnpj)
                DO
                UPDATE SET
                    nome = '{company.nome}',
                    cidade = '{company.cidade}',
                    estado = '{company.estado}'
        """

        try:
            cursor.execute(sql)
            self.connection.commit()
            print(
                f'O CNPJ {company.cnpj} foi'
                f'inserido com sucesso na base de dados!'
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.connection.rollback()
            cursor.close()
        cursor.close()

    def close_connection(self):
        self.connection.close()
