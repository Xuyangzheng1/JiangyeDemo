# Generated by Django 4.0.4 on 2022-08-16 02:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moviesList', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviesinformation',
            name='movies_posts',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='movie',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='moviesList.moviesinformation', verbose_name='movies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movie_imdbid',
            field=models.CharField(max_length=1024, null=True, verbose_name=' movieimdbid'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movie_imdblink',
            field=models.CharField(max_length=1024, null=True, verbose_name=' movieimdblink'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movie_introduction',
            field=models.TextField(max_length=10240, null=True, verbose_name='movieintroduction'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movie_natflixlink',
            field=models.CharField(max_length=1024, null=True, verbose_name=' movienatflixlink'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movie_runtime',
            field=models.CharField(max_length=255, null=True, verbose_name=' movieruntime'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movies_add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movies_country',
            field=models.CharField(max_length=32, null=True, verbose_name='moviecountry'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movies_language',
            field=models.CharField(max_length=32, null=True, verbose_name='movielanguage'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movies_matlevel',
            field=models.CharField(max_length=225, null=True, verbose_name='moviesmatlevel'),
        ),
        migrations.AddField(
            model_name='moviesinformation',
            name='movies_suggestions',
            field=models.CharField(max_length=225, null=True, verbose_name='moviesuggestions'),
        ),
        migrations.AlterField(
            model_name='moviesinformation',
            name='movies_title',
            field=models.TextField(max_length=225, null=True, verbose_name='moviename'),
        ),
        migrations.AlterField(
            model_name='moviesinformation',
            name='release_data',
            field=models.IntegerField(blank=True, default=2022, null=True),
        ),
        migrations.DeleteModel(
            name='BlogPost2',
        ),
    ]
