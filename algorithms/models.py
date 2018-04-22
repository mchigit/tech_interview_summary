from django.db import models

# Create your models here.


class Algorithm(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    implementation = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
