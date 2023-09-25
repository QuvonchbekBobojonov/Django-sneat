from django import template
from django.contrib.admin.templatetags.base import InclusionAdminNode

register = template.Library()


@register.tag(name="moorfo_admin_change_list_object_tools")
def change_list_object_tools_tag(parser, token):
    """Display the row of change list object tools."""
    return InclusionAdminNode(
        parser,
        token,
        func=lambda context: context,
        template_name="change_list_object_tools.html",
    )
