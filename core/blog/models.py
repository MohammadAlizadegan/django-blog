from django.db import models

class Post(models.Model):
    '''
    This is a class to define posts for blog app.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    '''
    This is a class to define categories for blog app.
    '''
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name