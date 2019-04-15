# Generated by Django 2.2 on 2019-04-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='cards',
            field=models.ManyToManyField(blank=True, null=True, related_name='list', to='api.Card'),
        ),
    ]