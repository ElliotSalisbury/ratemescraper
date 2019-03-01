# Generated by Django 2.1.7 on 2019-02-25 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProcessingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.TextField()),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objctify.ImageProcessingRequest')),
            ],
        ),
    ]
