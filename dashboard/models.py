from django.db import models

# Create your models here.

# File Upload Model.
class Files(models.Model):
    name = models.CharField(max_length=50, blank=True)
    File = models.FileField(upload_to='media/uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.File.delete()
        super().delete(*args, **kwargs)
