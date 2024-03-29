# Generated by Django 4.2.11 on 2024-03-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeOKVED', models.CharField(max_length=10, verbose_name='Код ОКВЭД')),
                ('Name', models.CharField(max_length=300, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='OccupationGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeOKZ', models.CharField(max_length=4, verbose_name='Код ОКЗ')),
                ('Name', models.CharField(max_length=300, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodePS', models.CharField(max_length=2, verbose_name='Код ПС')),
                ('FullCode', models.CharField(max_length=15, verbose_name='Полный Код')),
                ('Name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('RegNumber', models.CharField(max_length=20, verbose_name='Регистрационный номер')),
                ('Goal', models.TextField(verbose_name='Основная цель вида профессиональной деятельности')),
                ('EconomicActivity', models.ManyToManyField(to='importstandart.economicactivity', verbose_name='Виды экономической деятельности')),
                ('OccupationGroup', models.ManyToManyField(to='importstandart.occupationgroup', verbose_name='Группа занятий')),
            ],
        ),
    ]
