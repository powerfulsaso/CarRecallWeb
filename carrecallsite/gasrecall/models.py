from django.db import models
import datetime

# Create your models here.


class GasHistory(models.Model):
    purchase_date = models.DateTimeField('Purchase Date')
    gas_amount = models.FloatField('Gas Amount')
    paid_amount = models.FloatField('Paid Amount')
    tachometer = models.IntegerField('Tachometer')
    last_tachometer = models.IntegerField('Last Tachometer')

    def gas_price(self):
        return self.paid_amount/self.gas_amount

    def gas_consumption(self):
        if self.tachometer > self.last_tachometer:
            fuel_consumption = (self.gas_amount / (self.tachometer - self.last_tachometer)) * 100
            return fuel_consumption

    def days_ago(self):
        return (datetime.datetime.now() - self.purchase_date).days

    def __str__(self):
        s = "Id = {0:09d} \t| Date = {1:s} \t| GasAmount = {2:3.3f}" \
            " \t| GasPrice = {3:3.2f} \t| Tachometer = {4:d}".format(self.id, str(self.purchase_date), self.gas_amount,
                                                                     self.gas_price(), self.tachometer)
        return s
