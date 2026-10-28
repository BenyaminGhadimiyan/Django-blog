from django.db import models

class Contact(models.Model) :
    name=models.CharField(max_length=155)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    date=models.DateField(auto_now=True)
    update_date=models.DateField(auto_now=True)

    class Meta() :
        ordering=['date']

    def __str__(self) :
        return f"{self.name} - {self.id}"

