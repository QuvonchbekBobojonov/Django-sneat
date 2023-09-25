from django import template
from django.conf import settings
from django.contrib.admin.views.main import PAGE_VAR
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from ..apps import MoorfoAdminConfig

register = template.Library()


@register.simple_tag
def paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    if i == cl.paginator.ELLIPSIS:
        return format_html('<li class="page-item active" aria-disabled="true"><span class="page-link" aria-hidden="true">{}</span></li>', cl.paginator.ELLIPSIS)
    elif i == cl.page_num:
        return format_html('<li class="page-item active" aria-disabled="true"><span class="page-link" aria-hidden="true">{}</span></li>', i)
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
