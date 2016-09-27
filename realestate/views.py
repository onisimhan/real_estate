import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from realestate import models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from realestate.serializers import MainSerializer, MainRemovedSerializer, MainAdvancedSeralizer
from realestate.paginators import SmallResultsSetPagination
from .forms import ContactForm, ContactUsForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
import operator
from django.db.models import Q
from django.db.models.aggregates import Count
from random import randint



class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        def random(self):
            count = self.aggregate(count=Count('id'))['count']
            random_index = randint(0, count - 1)
            return self.all()[random_index]

        context = super(HomeView, self).get_context_data(*args, **kwargs)
        rand = []
        for n in range(0,5):
            p = random(models.Main.objects)
            rand.append(p)
        context['properties'] = rand
        return context


class StateListView(generic.ListView):
    template_name = 'state_list.html'
    queryset = models.Main.objects.filter(
        available=True, state__isnull=False).distinct('state').exclude(
        state='').order_by('city')


class PropertyListView(generic.ListView):
    template_name = 'property_list.html'
    paginate_by = 16

    def get_queryset(self):
        return models.Main.objects.filter(
            state=self.kwargs.get('s', ''),
            city=self.kwargs.get('c', '').replace('-', ' '))


class CityListView(generic.ListView):
    template_name = 'city_list.html'
    paginate_by = 16

    def get_queryset(self):
        return get_list_or_404(
            models.City.objects.filter(state=self.kwargs.get('s', '')).order_by('name'))


def old_property_view(request, **kwargs):
    # Get the available properties for the given state and city
    main = models.Main.objects.filter(
        state=kwargs.get('s', ''),
        city__icontains=kwargs.get('c', '').replace('-', ' '),
        available=True)
    # Filter objects by each word in the given address
    address_q = kwargs.get('a', '').replace('-', ' ').split(' ')
    query = reduce(
        operator.and_, (Q(address__icontains=item) for item in address_q))
    main_property = get_object_or_404(main, query)
    return redirect(main_property)


class PropertyView(generic.DetailView):
    template_name = 'index.html'
    model = models.Main
    context_object_name = 'main_data'
    pk_url_kwarg = 'pk'

## API Views
class MainViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Main.objects.all()
    serializer_class = MainSerializer

    def get_queryset(self):
        params = {k: v for k, v in self.request.query_params.items()}
        params['available'] = True
        if 'days_posted' in params.keys():
            filter_day = datetime.timedelta(
                days=int(params.get('days_posted')))
            filter_by = datetime.date.today() - filter_day
            params['create_date__gte'] = filter_by
            params.pop('days_posted')

        queryset = models.Main.objects.filter(**params)
        return queryset


class MainRemovedViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.MainRemoved
    queryset = models.MainRemoved.objects.all()
    serializer_class = MainRemovedSerializer

    def get_queryset(self):
        params = {k: v for k, v in self.request.query_params.items()}
        if 'days_removed' in params.keys():
            filter_day = datetime.timedelta(
                days=int(params.get('days_removed')))
            filter_by = datetime.date.today() - filter_day
            params['date_removed__gte'] = filter_by
            params.pop('days_removed')

        queryset = models.MainRemoved.objects.filter(**params)
        return queryset

class MainAdvancedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainAdvancedSeralizer
    pagination_class = SmallResultsSetPagination
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        params = {k: v for k, v in self.request.query_params.items()}
        params['available'] = True
        if 'days_posted' in params.keys():
            filter_day = datetime.timedelta(
                days=int(params.get('days_posted')))
            filter_by = datetime.date.today() - filter_day
            params['create_date__gte'] = filter_by
            params.pop('days_posted')

        queryset = models.Main.objects.filter(**params)
        return queryset


## Static Page views
class MainContact(generic.FormView):
    template_name = 'emails/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        obj = form.cleaned_data

        custumer_content = render_to_string('emails/customer_message.html', {
            'name': obj['name'],
        })
        custumer_text_content = strip_tags(custumer_content)
        # Subject, Content, EmailFrom, EmailTo, ReplyTo
        custumer_email = EmailMultiAlternatives(
            u'Contact from SeeThisProperty', custumer_text_content,
            'contact@seethisproperty.com', [obj['email']],
            headers={'Reply-To': 'contact@seethisproperty.com'})
        custumer_email.attach_alternative(custumer_content, 'text/html')
        custumer_email.send()

        our_content = render_to_string('emails/our_message.html', {
            'name': obj['name'],
            'phone': obj['phone'],
            'email': obj['email'],
            'url': self.request.META['HTTP_REFERER']
        })
        our_text_content = strip_tags(our_content)
        # Subject, Content, EmailFrom, EmailTo, ReplyTo
        our_email = EmailMultiAlternatives(
            u'Contact from SeeThisProperty', our_text_content,
            'contact@seethisproperty.com', ['contact@seethisproperty.com'],
            headers={'Reply-To': obj['email']})
        our_email.attach_alternative(our_content, 'text/html')
        our_email.send()
        return JsonResponse({'message': 'success'})

class googledc6ee21d00cd442a(generic.TemplateView):
    template_name='googledc6ee21d00cd442a.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'


class TermsView(generic.TemplateView):
    template_name = 'terms_of_use.html'


class PrivacyView(generic.TemplateView):
    template_name = 'privacy.html'


class ContactUsView(generic.FormView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact_us')

    def form_valid(self, form):
        obj = form.cleaned_data

        try:
            custumer_content = render_to_string(
                'emails/customer_message.html', {
                    'name': obj['name'], })
            custumer_text_content = strip_tags(custumer_content)
            # Subject, Content, EmailFrom, EmailTo, ReplyTo
            custumer_email = EmailMultiAlternatives(
                u'Contact from SeeThisProperty', custumer_text_content,
                'contact@seethisproperty.com', [obj['email']],
                headers={'Reply-To': 'contact@seethisproperty.com'})
            custumer_email.attach_alternative(custumer_content, 'text/html')
            custumer_email.send()

            our_content = render_to_string(
                'emails/our_message_contact_us.html', {
                    'name': obj['name'],
                    'phone': obj['phone'],
                    'email': obj['email'],
                    'message': obj['message']})
            our_text_content = strip_tags(our_content)
            # Subject, Content, EmailFrom, EmailTo, ReplyTo
            our_email = EmailMultiAlternatives(
                u'Contact from SeeThisProperty', our_text_content,
                'contact@seethisproperty.com', ['contact@seethisproperty.com'],
                headers={'Reply-To': obj['email']})
            our_email.attach_alternative(our_content, 'text/html')
            our_email.send()
            messages.success(self.request, "Thanks for contacting us, we'll get back to you as soon as possible.")
        except:
            messages.error(self.request, "Sorry, something is wrong with our mail server and we couldn't get your message, please try again later.", extra_tags='danger')
        return super(ContactUsView, self).form_valid(form)
