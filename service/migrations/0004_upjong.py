# Generated by Django 2.2.4 on 2020-09-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_corona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upjong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CTY_NM', models.CharField(default='cty2', max_length=100)),
                ('WEEK_UPJONG', models.CharField(max_length=100)),
            ],
        ),
    ]