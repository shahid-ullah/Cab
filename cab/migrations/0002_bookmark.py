# Generated by Django 3.0.6 on 2020-05-30 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(editable=False)),
                ('snippet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cab.Snippet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cab_bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]