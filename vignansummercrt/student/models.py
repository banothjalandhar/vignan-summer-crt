from django.db import models
class student_model(models.Model):
    name=models.CharField(max_length=100)
    phno=models.CharField(max_length=10)
    def __str__(self):
        return self.name