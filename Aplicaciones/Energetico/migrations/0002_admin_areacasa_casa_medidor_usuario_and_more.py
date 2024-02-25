# Generated by Django 4.2.4 on 2024-02-22 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Energetico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AreaCasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArea', models.CharField(max_length=255)),
                ('listaElectrodomestico', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamaño', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Medidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipoMedicion', models.CharField(max_length=255)),
                ('datoConsumo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Electrodomestico',
        ),
        migrations.CreateModel(
            name='CalculadoraCosto',
            fields=[
                ('medidor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Energetico.medidor')),
                ('gastoEnergetico', models.FloatField()),
                ('gastoMonetario', models.FloatField()),
            ],
            bases=('Energetico.medidor',),
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('calculadoracosto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Energetico.calculadoracosto')),
                ('tiempo', models.CharField(max_length=255)),
            ],
            bases=('Energetico.calculadoracosto',),
        ),
        migrations.CreateModel(
            name='Grafico',
            fields=[
                ('calculadoracosto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Energetico.calculadoracosto')),
                ('tipo', models.CharField(max_length=255)),
            ],
            bases=('Energetico.calculadoracosto',),
        ),
    ]