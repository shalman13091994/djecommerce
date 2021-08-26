
# To make the categories available in all templates
# we have created context_processor from the settings django.contrib.messages.context_processors.messages

from .models import Category

def categories(request):
    return {
        'categories': Category.objects.all()
    }
