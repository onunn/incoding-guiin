# Generated by Django 3.2.7 on 2021-09-04 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mukbang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_classifier', models.CharField(max_length=2)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='muckbang',
            name='description',
        ),
        migrations.AlterField(
            model_name='muckbang',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mukbang.group'),
        ),
    ]
