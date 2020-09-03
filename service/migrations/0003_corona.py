# Generated by Django 2.2.4 on 2020-08-31 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20200830_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CTY_NM', models.CharField(default='cty2', max_length=100)),
                ('CO2', models.FloatField()),
                ('CO3', models.FloatField()),
                ('CO4', models.FloatField()),
                ('CO5', models.FloatField()),
                ('CO6', models.FloatField()),
                ('CO7', models.FloatField()),
                ('CO8', models.FloatField()),
            ],
        ),
    ]