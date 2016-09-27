# coding:utf-8
from django.core.management.base import BaseCommand
from realestate import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Get all cities with available properties
        cities = models.Main.objects.all().order_by('city').distinct('city')

        cities_dict = [
            {'city': x.city, 'state': x.state, 'available': x.available}
            for x in cities]

        c_count = 0  # created count
        u_count = 0  # updated count
        t_count = 0  # total count
        for city in cities_dict:
            city_name = city.get('city', 'blank')
            state_abbr = city.get('state', 'blank')
            obj, created = models.City.objects.get_or_create(
                name=city_name,
                state=state_abbr)
            if created:
                c_count += 1
            else:
                if obj.available != city.get('available', False):
                    u_count += 1
            obj.available = city.get('available', False)
            image_url = ''

            try:
                image_url = models.Main.objects.filter(
                    city=city_name,
                    state=state_abbr,
                    available=True)[0].image.all()[0].url
            except:
                print('Failed to get image_url for {}'.format(city_name))

            obj.image = image_url
            obj.save()
            t_count += 1

        msg = 'END!{0} cities created and {1} updated'.format(c_count, u_count)
        print(msg)
