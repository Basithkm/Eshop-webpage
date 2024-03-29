# Generated by Django 4.2 on 2023-05-02 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CategoryModel',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='city',
            name='district',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.AddField(
            model_name='district',
            name='city',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='app.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='app.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='district',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='app.district'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1', max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='app.category'),
            preserve_default=False,
        ),
    ]
