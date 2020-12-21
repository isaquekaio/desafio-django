import csv
from moduloadministrativo.models import Municipio


def csv_to_list(filename: str) -> list:

    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):

    aux = []
    for item in data:
        pk = item.get('Codigo_Municipio')
        nome = item.get('Nome_Municipio')
        uf = item.get('UF')
        obj = Municipio(
            pk=pk,
            mome=nome,
            uf=uf,
        )
        aux.append(obj)
    Municipio.objects.bulk_create(aux)


data = csv_to_list('dados_importacao_projeto_1/municipios_ibge.csv')
save_data(data)