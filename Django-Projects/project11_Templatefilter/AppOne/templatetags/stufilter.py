from django import template
register = template.Library()


@register.filter(name='stulower')
def Stufilter(value):
    result = value[:1].upper()
    return result

# register.filter('stulower',Stufilter)

# Make sure you are not missing any of the following steps:
#
# Create a folder called "templatetags" at the same level as models.py and views.py in your application folder
#
# Your application must be in the INSTALLED_APPS in settings.py
#
# The templatetags folder must have __init__.py
#
# Restart the django server