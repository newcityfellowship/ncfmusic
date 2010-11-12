'''
 From django_annoying @ http://bitbucket.org/offline/django-annoying/src/tip/annoying/functions.py
 Copied here to use it without needing one more app installed on PYTHONPATH
'''
def get_object_or_None(klass, *args, **kwargs):
  from django.shortcuts import _get_queryset
    
  queryset = _get_queryset(klass)
  try:
    return queryset.select_related().get(*args, **kwargs)
  except queryset.model.DoesNotExist:
    return None