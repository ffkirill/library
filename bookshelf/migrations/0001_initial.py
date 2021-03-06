# Generated by Django 3.1.4 on 2021-01-11 20:15

from django.db import migrations, models
import django.db.models.deletion
import ool


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', ool.VersionField(default=0)),
                ('title', models.CharField(max_length=256, verbose_name='Bookshelf name')),
            ],
            bases=(ool.VersionedMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BookshelfItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pos_numerator', models.IntegerField(verbose_name='Position(numerator)')),
                ('pos_denominator', models.IntegerField(verbose_name='Position(denominator)')),
                ('version', ool.VersionField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('bookshelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookshelf', verbose_name='Bookshelf')),
            ],
            options={
                'unique_together': {('pos_numerator', 'pos_denominator')},
            },
            bases=(ool.VersionedMixin, models.Model),
        ),
    ]
