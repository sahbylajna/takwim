# Generated by Django 4.2.7 on 2023-11-14 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post', models.TextField()),
                ('notes', models.TextField()),
                ('type', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_evaluations', to='Client.clientuser')),
                ('evaluator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respo_evaluations', to='Client.clientuser')),
            ],
        ),
    ]
