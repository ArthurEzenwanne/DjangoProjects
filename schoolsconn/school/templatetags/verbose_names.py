from django import template

register = template.Library()

@register.simple_tag
def get_verbose_field_name(instance, field_name):
    ''' Returns verbose name for a field. '''
    #return instance._meta.get_field(field_name).verbose_name.title()
    # Removed the .title() so that the verbose names cames out as defined
    return instance._meta.get_field(field_name).verbose_name