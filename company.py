class Company:

    def __init__(self, cnpj, nome=None, cidade=None, estado=None):
        cnpj = str(cnpj)
        cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
        if self.cnpj_is_valid(cnpj):
            self.cnpj = cnpj
            self.nome = nome
            self.cidade = cidade
            self.estado = estado
        else:
            raise ValueError('CNPJ Inválido!')

    def cnpj_is_valid(self, cnpj):
        if len(cnpj) == 14:
            return True
        else:
            return False

    def update_attributes(self, nome, cidade, estado):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return self.cnpj
