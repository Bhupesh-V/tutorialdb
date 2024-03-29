# Generated by Django 2.2.3 on 2019-08-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='category',
            field=models.CharField(choices=[('article', 'Article'), ('book', 'Book'), ('cheatsheet', 'Cheatsheet'), ('course', 'Course'), ('docs', 'Documentation'), ('video', 'Video')], max_length=20),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
