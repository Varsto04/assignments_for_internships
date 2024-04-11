from django import template
from menuapp.models import MenuElement
import copy

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    url_path = context['request'].path.split('/')
    url = "/tree/"
    menu_items = MenuElement.objects.filter(parent=None, name_menu=menu_name)
    menu_html = '<ul>'
    for item in menu_items:
        url += item.title
        menu_html += f'<a href="{url}"><li>{item.title}</li></a>'
        url += '/'
        menu_html += draw_children(item, url, url_path)
        url = ""
    menu_html += '</ul>'
    return menu_html


def draw_children(parent, url, url_path):
    children_html = ''
    children = MenuElement.objects.filter(parent=parent)
    url2 = copy.copy(url)
    if children:
        children_html += '<ul>'
        for child in children:
            url += child.title
            children_html += f'<a href="{url}"><li>{child.title}</li></a>'
            url += '/'
            if str(child) == str(url_path[-1]):
                children_html += draw_children(child, url, url_path)
                url += '/'
            url = url2
        children_html += '</ul>'
    return children_html
