from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    language = models.CharField(default="python", max_length=50)
    
    class Meta:
        ordering = ["created"]