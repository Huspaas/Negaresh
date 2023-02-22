from django.db import models
from django.contrib.auth.models import User

class contract(models.Model):
    clientName = models.CharField(max_length=50 , verbose_name='نام مشتری')
    dealer = models.CharField(max_length=50 , verbose_name='نام کارشناس')
    clientNumber = models.CharField(max_length=11 , verbose_name='شماره مشتری' , unique=True)
    time = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , verbose_name='منتشرکننده')

    
 
   
   
    def __str__(self):
        return self.clientName


    class Meta:
        verbose_name='قرارداد'
        verbose_name_plural = 'قرارداد ها'

