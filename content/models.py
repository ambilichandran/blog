from django.db import models
class Post(models.Model):
    title=models.CharField(max_length=50,blank=False)
    image=models.ImageField(upload_to="image/")
    content=models.TextField(max_length=500,blank=False)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.title
