# Generated by Django 3.1.7 on 2021-03-17 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbsnote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbsnote.board')),
            ],
        ),
    ]
