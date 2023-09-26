from django import template
from django.conf import settings
from django.contrib.admin.views.main import PAGE_VAR
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.apps import apps

from typing import Dict

from ..apps import MoorfoAdminConfig

register = template.Library()


@register.simple_tag
def header_class(header: Dict, forloop: Dict) -> str:
    """
    Adds CSS classes to header HTML element depending on its attributes
    """
    classes = []
    sorted, asc, desc = (
        header.get("sorted"),
        header.get("ascending"),
        header.get("descending"),
    )

    is_checkbox_column_conditions = (
        forloop["counter0"] == 0,
        header.get("class_attrib") == ' class="action-checkbox-column"',
    )
    if all(is_checkbox_column_conditions):
        classes.append("djn-checkbox-select-all")

    if not header["sortable"]:
        return " ".join(classes)

    if sorted and asc:
        classes.append("sorting_asc")
    elif sorted and desc:
        classes.append("sorting_desc")
    else:
        classes.append("sorting")

    return " ".join(classes)


@register.simple_tag
def available_apps():
    available_apps_list = []
    for app_config in apps.get_app_configs():
        app_name = app_config.verbose_name
        models = app_config.get_models()
        available_apps_list.append({'name': app_name, 'models': models})
    return available_apps_list


@register.simple_tag
def paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    if i == cl.paginator.ELLIPSIS:
        return format_html(
            '<li class="page-item disabled" aria-disabled="true"><span class="page-link" aria-hidden="true">{}</span></li>',
            cl.paginator.ELLIPSIS)
    elif i == cl.page_num:
        return format_html(
            '<li class="page-item active" aria-disabled="true"><span class="page-link" aria-hidden="true">{}</span></li>',
            i)
    else:
        return format_html(
            '<li class="page-item" aria-disabled="true"><a href="{}" {} aria-hidden="true">{}</a></li>',
            cl.get_query_string({PAGE_VAR: i}),
            mark_safe('class="page-link end"' if i == cl.paginator.num_pages else 'class="page-link"'),
            i,
        )


@register.simple_tag
def get_copyright():
    data = settings.MOORFOADMIN_SETTINGS['copyright']
    return data


@register.simple_tag
def get_version():
    data = MoorfoAdminConfig.version
    return data
