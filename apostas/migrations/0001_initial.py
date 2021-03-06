# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('primeirotime', models.IntegerField(verbose_name='primeirotime')),
                ('segundotime', models.IntegerField(verbose_name='segundotime')),
                ('data', models.DateField(auto_now_add=True, verbose_name='data')),
                ('pontos', models.IntegerField(blank=True, null=True, verbose_name='pontos')),
            ],
            options={
                'db_table': 'aposta',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
            ],
            options={
                'db_table': 'campeonato',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('resultadoprimeirotime', models.IntegerField(blank=True, null=True, verbose_name='resultadoprimeirotime')),
                ('resultadosegundotime', models.IntegerField(blank=True, null=True, verbose_name='resultadosegundotime')),
                ('data', models.DateField(auto_now_add=True, verbose_name='data')),
                ('calculado', models.BooleanField(verbose_name='calculado')),
                ('datajogo', models.DateField(null=True, verbose_name='datajogo')),
                ('rodada', models.IntegerField(null=True, blank=True, verbose_name='rodada')),
                ('horajogo', models.TimeField(null=True, verbose_name='horajogo')),
                ('campeonato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apostas.Campeonato')),
            ],
            options={
                'db_table': 'jogo',
                'ordering': ['-datajogo', 'calculado', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('brasao', models.CharField(max_length=255, verbose_name='brasao')),
            ],
            options={
                'db_table': 'time',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('login', models.EmailField(max_length=255, verbose_name='login')),
                ('senha', models.CharField(max_length=32, verbose_name='senha')),
                ('ranking', models.IntegerField(verbose_name='ranking')),
                ('ativo', models.BooleanField(verbose_name='ativo')),
            ],
            options={
                'db_table': 'usuario',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='usuario',
            unique_together=set([('login',)]),
        ),
        migrations.AddField(
            model_name='jogo',
            name='primeirotime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='primeirotime', to='apostas.Time'),
        ),
        migrations.AddField(
            model_name='jogo',
            name='segundotime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='segundotime', to='apostas.Time'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apostas.Jogo'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apostas.Usuario'),
        ),
    ]
