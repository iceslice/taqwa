from django import template
import re

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Usage: {{ my_dict|get_item:key }} — Django templates can't do
    dict[key] with a variable key out of the box, so this fills the gap.
    Used on the CRM dashboard to show a live count per pipeline status."""
    if not dictionary:
        return 0
    return dictionary.get(key, 0)



@register.filter
def digits_only(value):
    """Strip everything except digits — used for wa.me links, since
    WhatsApp click-to-chat requires a bare digit string with no +,
    spaces, or dashes, but admins often type numbers formatted for
    readability."""
    if not value:
        return ""
    return re.sub(r"\D", "", str(value))