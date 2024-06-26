# Generated by Django 5.0.5 on 2024-06-07 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instituicao', '0001_initial'),
        ('tipo_evento', '0002_alter_tipoevento_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, help_text='* Campo obrigatório', max_length=150, unique=True, verbose_name='Nome do evento *')),
                ('data_inicio', models.DateField(help_text='Use dd/mm/aaaa', max_length=10, verbose_name='Data de início do evento *')),
                ('data_limite_trabalhos', models.DateField(help_text='Use dd/mm/aaaa', max_length=10, verbose_name='Data limite para envio de trabalhos *')),
                ('modelo_artigo', models.CharField(help_text='Informe o modelo, como ABNT, SBC, IEEE', max_length=150, verbose_name='Qual o modelo para artigos? ')),
                ('arquivo_modelo', models.FileField(blank=True, help_text='Utilize arquivo compactado do tipo zip', null=True, upload_to='midias', verbose_name='Carregue arquivo zipado com modelos')),
                ('is_active', models.BooleanField(default=True, help_text='Se ativo, o evento está liberado para chamada de artigos', verbose_name='Ativo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
                ('coordenador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='coordenador', to=settings.AUTH_USER_MODEL, verbose_name='Coordenador responsável *')),
                ('coordenador_suplente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='coordenador_suplente', to=settings.AUTH_USER_MODEL, verbose_name='Coordenador suplente')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instituicao', to='instituicao.instituicao', verbose_name='Instituição responsável pelo evento *')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipo_evento', to='tipo_evento.tipoevento', verbose_name='Tipo do evento *')),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
                'ordering': ['-is_active', '-data_limite_trabalhos', 'nome'],
            },
        ),
    ]
