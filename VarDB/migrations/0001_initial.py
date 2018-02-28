# Generated by Django 2.0.2 on 2018-02-28 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('investigation_date', models.DateTimeField(verbose_name='date investigated')),
            ],
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(default=0, help_text='Enter cancer stage number')),
                ('description', models.CharField(max_length=200)),
                ('age_occurrence', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('registration_date', models.DateTimeField(verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='Refseq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50)),
                ('refseq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDB.Gene')),
            ],
        ),
        migrations.AddField(
            model_name='occurrence',
            name='occurrence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDB.Patient'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='investigation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDB.Occurrence'),
        ),
        migrations.AddField(
            model_name='gene',
            name='gene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDB.Investigation'),
        ),
    ]