from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
      STATUS_CHOICES =(('eur/usd','eur/usd'),('gbp/usd','gbp/usd'),('jpy/usd','jpy/usd'),)
      user = models.CharField(max_length=50,blank=True,null=True)
      pair = models.CharField(max_length=10,choices=STATUS_CHOICES,default='eur/usd')
      lot_size = models.CharField(max_length=10,default='0.01')
      entry = models.CharField(max_length=10,blank=True,null=True)
      close = models.CharField(max_length=10,blank=True,null=True)
      profit = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
      loss = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
      entry_time = models.TimeField()
      close_time = models.TimeField()
      date = models.DateField(auto_now_add=True)
      notes = models.TextField(blank=True,null=True)

      def __str__(self):
          return f'{self.user} - {self.lot_size}'
# Create your models here.
