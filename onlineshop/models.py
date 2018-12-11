from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):

    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)

    def create(self):
        self.save()

    def __str__(self):
        return self.cat_name

class Good(models.Model):

    good_id = models.AutoField(primary_key=True)
    good_name = models.CharField(max_length=200)
    good_cat_id = models.ForeignKey('Category',
        on_delete=models.CASCADE,)
    good_description = models.TextField()


    def create(self):
        self.save()

    def __str__(self):
        return self.good_name
