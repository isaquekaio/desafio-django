# Generated by Django 3.1.4 on 2020-12-21 12:16

from django.db import migrations, models

def load_data(apps, schema_editor):
    Uf = apps.get_model("moduloadministrativo","Uf")

    Uf(11, "Rondônia").save()
    Uf(12, "Acre").save()
    Uf(13, "Amazonas").save()
    Uf(14, "Roraima").save()
    Uf(15, "Pará").save()
    Uf(16, "Amapá").save()
    Uf(17, "Tocantins").save()
    Uf(21, "Maranhão").save()
    Uf(22, "Piauí").save()
    Uf(23, "Ceará").save()
    Uf(24, "Rio Grande do Norte").save()
    Uf(25, "Paraíba").save()
    Uf(26, "Pernambuco").save()
    Uf(27, "Alagoas").save()
    Uf(28, "Sergipe").save()
    Uf(29, "Bahia").save()
    Uf(31, "Minas Gerais").save()
    Uf(32, "Espírito Santo").save()
    Uf(33, "Rio de Janeiro").save()
    Uf(35, "São Paulo").save()
    Uf(41, "Paraná").save()
    Uf(42, "Santa Catarina").save()
    Uf(43, "Rio Grande do Sul").save()
    Uf(50, "Mato Grosso do Sul").save()
    Uf(51, "Mato Grosso").save()
    Uf(52, "Goiás").save()
    Uf(53, "Distrito Federal").save()

class Migration(migrations.Migration):

    dependencies = [
        ('moduloadministrativo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
