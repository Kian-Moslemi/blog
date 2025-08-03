from django import template
from posts.models import Article
from datetime import datetime

register = template.Library()

@register.simple_tag
def count_of_blog():
    return Article.publish.count()


@register.filter(name='new')
def blog(value):
    created_date = value.strftime('%d %m %y')
    now_date = datetime.now().strftime('%d %m %y')
    created_prime = datetime.strptime(created_date,'%d %m %y')
    now_prime = datetime.strptime(now_date,'%d %m %y')
    if (now_prime - created_prime).days < 7:
        return ('NEW')
    else:
        return('')

    

