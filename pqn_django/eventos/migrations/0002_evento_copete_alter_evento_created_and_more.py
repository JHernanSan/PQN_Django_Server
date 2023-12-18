# Generated by Django 5.0 on 2023-12-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='copete',
            field=models.TextField(max_length=100, null=True, verbose_name='Copete del evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha subido'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='picture',
            field=models.ImageField(upload_to='eventos', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Título de Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Ultima actualización'),
        ),
    ]
