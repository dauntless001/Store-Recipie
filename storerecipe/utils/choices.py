from django.db import models

class Gender(models.TextChoices):
    Male = ("male", "Male")
    Female = ("female", "Female")
    Other = ("other", "Other")

class Marital(models.TextChoices):
    Married = ("married", "Married")
    Single = ("single", "Single")

class Status(models.TextChoices):
    Draft = ("draft", "Draft")
    Published = ("published", "Published")