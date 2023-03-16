from company import Company
from db import ConnectDb
from services.company_service import CompanyServices

company_service = CompanyServices()
data_base = ConnectDb()
array_cnpjs = [
    '82.110.818/0001-21',
    '82110818000202',
    '82110818000393'
]
companies = [Company(cnpj) for cnpj in array_cnpjs]

for company in companies:
    nome, cidade, estado = company_service.get_cnpj_data(company.cnpj)
    company.update_attributes(nome, cidade, estado)
    data_base.update_or_create_company(company)

data_base.close_connection()
