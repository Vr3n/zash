from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser
User = get_user_model()

# Create your models here.

# File Upload Model.


class Files(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=True)
    File = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # returns the database instance with name instead of id to make debugging/referrencing more easy.
    def __str__(self):
        return self.name

    # function for foreign key access t o save() function
    def save(self, *args, **kwargs):
        super(Files, self).save(*args, **kwargs)

    # Function delete files from media folder
    def delete(self, *args, **kwargs):
        self.File.delete()
        super().delete(*args, **kwargs)
