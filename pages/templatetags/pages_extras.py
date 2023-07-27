from django import template # registration of template tags
from pages.models import Page # importing the Page model

register = template.Library() # registering the template tags

@register.simple_tag # decorator to register the template tag

def get_page_list(): # function to get the list of pages
    pages = Page.objects.all() # getting all the pages
    return pages
