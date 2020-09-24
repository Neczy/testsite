from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Имя')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости' 
        ordering = ['-created_at']
    

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Имя', default="Неотсортированное")
    

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории' 
        ordering = ['id']

    def __str__(self):
        return self.title


