from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    moderated = models.BooleanField(default=False)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def getDescription(self):
        return self.description[0:100]


class Comment(models.Model):
    who = models.CharField(max_length=100)
    text = models.TextField()
    new = models.ForeignKey(News, on_delete=models.CASCADE)
