# Generated by Django 2.0.8 on 2019-09-05 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_institute', models.CharField(blank=True, max_length=50, null=True)),
                ('course', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('possed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='media/UserImages')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=265, null=True)),
                ('possed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_org', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('bio', models.TextField()),
                ('possed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]