from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=200)
    population = models.CharField(max_length=15)

    def __str__(self):
        return f"Counry name {self.country}, Population: {self.population}"

    class Meta:
        verbose_name_plural = "Country's population data"
