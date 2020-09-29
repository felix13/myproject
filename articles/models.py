from datetime import datetime

from django.contrib.auth.models import User
from django.db import models




class Article(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

   
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4000)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)
  
 
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        else:
            self.update_date = datetime.now()
            
        super().save(*args, **kwargs)

   


    
