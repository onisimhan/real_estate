# coding:utf-8
import urllib
from urlparse import urlparse
from django.core.management.base import BaseCommand
from realestate import models
from django.core.files import File


class Command(BaseCommand):

    def get_image_or_not(self, filename):
        try:
            return models.MainImage.objects.get(image=filename)
        except:
            return None

    def handle(self, *args, **options):
        # get all images urls
        images = models.Image.objects.all()
        total = images.count()
        count = 0
        print('Total of {} urls to download'.format(total))
        print('Repeated images will be skipped')

        for image in images:
            name = urlparse(image.url).path.split('/')[-1]
            content = urllib.urlretrieve(image.url, '/tmp/gather_images/{}'.format(image.url))
            filename = str(image.main.pk) + '/' + name

            # if the image was already downloaded, skip
            if self.get_image_or_not(filename):
                count += 1
                continue

            # if image was not downloaded yet. Save it
            new_image = models.MainImage()
            new_image.main = image.main
            with open(content[0]) as file_obj:
                new_image.image.save(name, File(file_obj), save=True)
            count += 1
            if count % 10 == 0:
                print('{} Downloaded, {} to go'.format(count, total))
