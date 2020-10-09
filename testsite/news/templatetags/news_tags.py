from django import template

from news.models import Category 

register = template.Library()

# тег регистрации категорий
@register.simple_tag(name='get_list_categories')
def get_gategories():
    return Category.objects.all()

#  тег включения категорий
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories" : categories}