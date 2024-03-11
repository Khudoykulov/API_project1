# Generated by Django 5.0.3 on 2024-03-11 17:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/')),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='recipe.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.IntegerField(choices=[(0, 'Kilogram'), (1, 'Gram'), (2, 'Litre'), (3, 'Piece')], default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipe.recipe')),
            ],
        ),
    ]
