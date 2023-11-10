from django.db import models


class Drug(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    diseases = models.ManyToManyField('Disease')
    description = models.TextField()
    name = models.CharField(max_length=255)
    released = models.DateField()

    def formatted_release_date(self):
        return self.released.strftime('%d/%m/%Y')

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
