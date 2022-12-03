# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Stocks(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open = models.FloatField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    ex_dividend = models.FloatField(db_column='Ex-Dividend', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    split_ratio = models.FloatField(db_column='Split Ratio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_open = models.FloatField(db_column='Adj. Open', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_high = models.FloatField(db_column='Adj. High', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_low = models.FloatField(db_column='Adj. Low', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_close = models.FloatField(db_column='Adj. Close', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_volume = models.FloatField(db_column='Adj. Volume', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stock = models.TextField(blank=True, null=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'stocks'
        app_label ='modles.Stocks'
