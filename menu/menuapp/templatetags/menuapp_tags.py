from django import template
from menuapp.models import MenuElement
import copy

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    url_path = context['request'].path.split('/')
    url = "/tree/"
    url_path.pop(0)
    url_path.pop(0)

    all_menu_elements = MenuElement.objects.filter(name_menu=menu_name)
    elements_dict = {element.id: element for element in all_menu_elements}
    root_elements = [element for element in all_menu_elements if not element.parent]

    menu_html = '<ul>'
    for item in root_elements:
        url += item.title
        menu_html += f'<a href="{url}"><li>{item.title}</li></a>'
        url += '/'
        if len(url_path) > 0:
            if str(item) == url_path[0]:
                url_path.pop(0)
                menu_html += draw_children(item, url, url_path, elements_dict)
        url = ""
    menu_html += '</ul>'
    return menu_html


def draw_children(parent_element, url, url_path, elements_dict):
    children_html = ''

    children = parent_element.children.all()

    url2 = copy.copy(url)

    if children:
        children_html += f'<ul>'
        for child in children:
            url += child.title
            children_html += f'<a href="{url}"><li>{child.title}</li></a>'
            url += '/'
            if len(url_path) > 0:
                if str(child) == str(url_path[0]):
                    url_path.pop(0)
                    children_html += draw_children(child, url, url_path, elements_dict)
                    url += '/'
                    url = url2
        children_html += '</ul>'

    return children_html
