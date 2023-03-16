import requests


class CompanyServices:

    def __init__(self):
        self.base_url = 'https://receitaws.com.br/v1/'

    def get_cnpj_data(self, cnpj):
        url = f'{self.base_url}cnpj/{cnpj}'
        r = requests.get(url)
        data = r.json()
        return (
            data['nome'],
            data['municipio'],
            data['uf']
        )
