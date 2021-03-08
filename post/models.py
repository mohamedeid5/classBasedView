from django.db import models

# Create your models here.

class Post(models.Model):
   
    title = models.CharField(max_length=190)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='post-img/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
