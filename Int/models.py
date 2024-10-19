from django.db import models

class Document(models.Model):
    #id = models.(max_length=100,auto_created=True)
    uploaded_file = models.FileField(upload_to='documents/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)