from django.db import models

class Post(models.Model):
    '''
    This is class to define posts for blog app.
    '''
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL,null=True)
    image = models.ImageField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    class meta:
        verbose_name ='پست'
        verbose_name_plural='پست ها'
        
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    class meta:
        verbose_name ='کتگوری'
        verbose_name_plural='کتگوری ها'
    
    