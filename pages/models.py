from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.
class Page(models.Model):
	title=models.CharField(max_length=50)
	content=models.TextField()
	last_update=models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		  
		  return reverse('page-detail', args=[str(self.id)])
#@receiver(pre_save, sender=Page)
#def get_full_name(self, *args, **kwargs):
#	self.last_update = models.DateField.auto_now()
    	
   
     
		