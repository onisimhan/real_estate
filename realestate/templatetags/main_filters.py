# coding:utf-8
from django import template
import us
from django.core.urlresolvers import resolve
from realestate.models import Main

register = template.Library()


@register.filter
def remove_float(value):
    '''Removes decimal numbers'''
    value = str(value)
    if '.' in value:
        return value[:value.index('.')]
    elif ',' in value:
        return value[:value.index(',')]
    else:
        return value


@register.inclusion_tag('paginator.html', takes_context=True)
def paginator(context, adjacent_pages=3):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    paginator = context['page_obj'].paginator
    pages = paginator._num_pages
    results_per_page = paginator.per_page
    this_page = context['page_obj'].number
    page_obj = context['page_obj']

    start = max(this_page - adjacent_pages, 1)
    if start <= 2:
        start = 1

    end = this_page + adjacent_pages + 1
    if end == pages:
        end = pages + 1

    has_next, has_previous = False, False

    if this_page < pages:
        has_next = True

    if this_page > 1:
        has_previous = True

    page_numbers = [n for n in range(start, end) if n > 0 and n <= pages]

    return {
        'page_obj': page_obj,
        'paginator': paginator,
        'results_per_page': results_per_page,
        'page': this_page,
        'pages': pages,
        'page_numbers': page_numbers,
        'next': this_page + 1,
        'previous': this_page - 1,
        'has_next': has_next,
        'has_previous': has_previous,
        'show_first': 1 not in page_numbers,
        'show_last': pages not in page_numbers,
    }


@register.simple_tag
def get_base_states():
    states = us.states.STATES
    statesObj = [{'name': i.name, 'abbr': i.abbr} for i in states]
    return statesObj


@register.filter
def lookup_state_name(state):
    '''Return the state name from the given abbr'''
    return us.states.lookup(state).name


@register.inclusion_tag('get_404_object.html')
def get_404_object(path):
    '''Return suggestions based on the requested path that resulted in 404'''
    try:
        if '/' not in path[-1]:
            path = path + '/'
        url_name = resolve(path).url_name
        kwargs = resolve(path).kwargs
    except:
        url_name = ''

    if url_name and url_name == 'property':
        return {
            '404_type': 'property',
            'properties': Main.objects.filter(
                available=True,
                state=kwargs['s'], city__icontains=kwargs['c'])[:5],
            'city': kwargs['c'],
            'state': kwargs['s']
        }
    elif url_name and url_name == 'property_list':
        return {
            '404_type': 'city',
            'properties': Main.objects.distinct_cities_at(
                state=kwargs.get('s'))[:5],
            'city': kwargs['c'],
            'state': kwargs['s']
        }
    else:
        return {
            'property_not_found': False,
            'properties': Main.objects.filter(
                available=True).order_by('?')[:5]}
