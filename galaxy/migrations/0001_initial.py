# Generated by Django 3.2.9 on 2021-11-17 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(blank=True, max_length=10)),
                ('mass', models.CharField(blank=True, max_length=10)),
                ('hair_color', models.CharField(blank=True, max_length=20)),
                ('skin_color', models.CharField(blank=True, max_length=20)),
                ('eye_color', models.CharField(blank=True, max_length=20)),
                ('birth_year', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('homeworld', models.CharField(blank=True, max_length=30)),
                ('film', models.CharField(blank=True, max_length=30)),
                ('species', models.CharField(blank=True, max_length=30)),
                ('vehicles', models.CharField(blank=True, max_length=30)),
                ('starships', models.CharField(blank=True, max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True, help_text="The date and time the movie'data was created.")),
                ('edited', models.DateTimeField(help_text='The date and time the movie was edited.', null=True)),
                ('url', models.URLField(help_text="The url's movie .")),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('episode_id', models.IntegerField()),
                ('opening_crawl', models.TextField(max_length=1000)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(help_text='The date and time the movie was released.', null=True)),
                ('created', models.DateTimeField(auto_now_add=True, help_text="The date and time the movie'data was created.")),
                ('edited', models.DateTimeField(help_text='The date and time the movie was edited.', null=True)),
                ('url', models.URLField(help_text="The url's movie .")),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rotation_period', models.CharField(max_length=50)),
                ('orbital_period', models.CharField(max_length=50)),
                ('diameter', models.CharField(max_length=50)),
                ('climate', models.CharField(max_length=50)),
                ('gravity', models.CharField(max_length=50)),
                ('terrain', models.CharField(max_length=50)),
                ('surface_water', models.CharField(max_length=50)),
                ('population', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, help_text="The date and time the movie'data was created.")),
                ('edited', models.DateTimeField(help_text='The date and time the movie was edited.', null=True)),
                ('url', models.URLField(help_text="The url's movie .")),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('classification', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('average_height', models.CharField(max_length=50)),
                ('skin_color', models.CharField(max_length=50)),
                ('hair_color', models.CharField(max_length=50)),
                ('eye_color', models.CharField(max_length=50)),
                ('average_lifespan', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('cost_in_credits', models.CharField(max_length=50)),
                ('length', models.CharField(max_length=50)),
                ('max_atmosphering_speed', models.CharField(max_length=50)),
                ('crew', models.CharField(max_length=50)),
                ('passengers', models.CharField(max_length=50)),
                ('cargo_capacity', models.CharField(max_length=50)),
                ('consumables', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_class', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Starships',
            fields=[
                ('transport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='galaxy.transport')),
                ('hyperdrive_hating', models.CharField(max_length=50)),
                ('MGLT', models.CharField(max_length=50)),
                ('starship_class', models.CharField(max_length=50)),
            ],
            bases=('galaxy.transport',),
        ),
    ]
