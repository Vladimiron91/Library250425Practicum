from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.last_name[0]}. {self.first_name}"