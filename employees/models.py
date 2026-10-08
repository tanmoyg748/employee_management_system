from django.db import models

class Employee(models.Model):
    name: models.CharField = models.CharField(max_length=100)
    email: models.EmailField = models.EmailField(unique=True)
    salary: models.DecimalField = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self) -> str:
        return self.name
