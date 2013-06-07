from django.db import models


DB_TYPE = (
    ('SC', 'Select'),
    ('SQ', 'Sqlite'),
    ('MY', 'Mysql'),
)


class Databases(models.Model):
    name = models.CharField(max_length=40, verbose_name='Database Name')
    db_type = models.CharField(max_length=2, choices=DB_TYPE, default='SC', verbose_name='Database Type')
    user = models.CharField(max_length=20, verbose_name='Database UserName')
    passwd = models.CharField(max_length=20, verbose_name='Database Password')
    host = models.CharField(max_length=40, verbose_name="Host")


class TablesData(models.Model):
    db = models.ForeignKey(Databases)
    name = models.CharField(max_length=40)
    row_count = models.IntegerField()
    column_count = models.IntegerField()
    decription = models.TextField()


class FieldData(models.Model):
    table = models.ForeignKey(TablesData)
    name = models.CharField(max_length=40)
    data_type = models.CharField(max_length=20)
    nullable = models.BooleanField()
    primary_key = models.BooleanField()
    foreign_key = models.BooleanField()
    decription = models.TextField()


class RecordData(models.Model):
    table = models.ForeignKey(TablesData)
    record = models.TextField()
