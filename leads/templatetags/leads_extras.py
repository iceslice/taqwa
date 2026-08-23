from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Usage: {{ my_dict|get_item:key }} — Django templates can't do
    dict[key] with a variable key out of the box, so this fills the gap.
    Used on the CRM dashboard to show a live count per pipeline status."""
    if not dictionary:
        return 0
    return dictionary.get(key, 0)
