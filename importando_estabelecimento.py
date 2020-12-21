import csv
from moduloadministrativo.models import Estabelecimento, Uf, Municipio


def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    aux = []
    for item in data:
        nome = item.get('NO_FANTASIA')
        cnes = item.get('CO_CNES')
        cnpj = item.get('NU_CNPJ')
        uf = Uf.objects.get(pk=int(item.get('CO_ESTADO_GESTOR')))
        municipio = Municipio.objects.get(pk=int(item.get('CO_MUNICIPIO_GESTOR')))
        obj = Estabelecimento(
            nome=nome,
            cnes=cnes,
            cnpj=cnpj,
            uf=uf,
            municipio=municipio,
        )
        aux.append(obj)
    Estabelecimento.objects.bulk_create(aux)


data = csv_to_list('dados_importacao_projeto_1/estabelecimentos_saude.csv')
save_data(data)