# Generated by Django 3.2.25 on 2024-10-09 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0002_profile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('Business', 'Business'), ('Technology', 'Technology'), ('Sports', 'Sports'), ('Food', 'Food'), ('Fashion', 'Fashion'), ('Others', 'Others')], max_length=50)),
                ('approved', models.BooleanField(null=True)),
                ('image', models.ImageField(null=True, upload_to='blogImages/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogApp.bloginfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blogApp.bloginfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.profile')),
            ],
            options={
                'unique_together': {('blog', 'user')},
            },
        ),
    ]
