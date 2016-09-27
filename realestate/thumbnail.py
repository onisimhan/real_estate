# coding:utf-8
import os
from PIL import Image
from django.core.files import File
from django.core.files.storage import default_storage as storage


class Thumbnailed(object):
    def __init__(self, file, thumbnail_size=(150, 150)):
        self.storage = storage
        self.thumbnail_size = thumbnail_size
        self.file = file
        self.image = Image.open(self.file.file)

        self.full_name = file.name
        self.filename = self.file.name.split('/')[-1]  # name without dir
        self.ext = '.' + self.full_name.split('.')[-1]  # file extension
        self.filename_noext = self.filename.replace('.' + self.ext, '')

        self.thumb_full = self.full_name.replace(self.ext, '') + '_thumb.jpg'
        self.thumb_name = self.filename.replace(self.ext, '') + '_thumb.jpg'
        self.thumb_url = self.storage.url(self.thumb_name)

    def convert_image_mode(self):
        # Convert to RGB if necessary
        if self.image.mode not in ('L', 'RGB'):
            try:
                self.image = self.image.convert('RGB')
            except:
                pass

    def compress_image(self, quality=70):
        self.convert_image_mode()
        try:
            self.image.save(self.filename, quality=quality)
        except Exception as e:
            print(e)

    def create_thumbnail(self, quality=70):
        self.convert_image_mode()
        thumb = self.image.copy()
        thumb.thumbnail(self.thumbnail_size)
        thumb.save(self.thumb_name)
        try:
            with open(self.thumb_name) as file_obj:
                self.storage.save(self.thumb_full, File(file_obj))
        except Exception as e:
            print(e)

    def garbage_collection(self):
        '''If you're using some remote storage use this after your save
        method to clean local files'''
        try:
            os.remove(self.filename)
            os.remove(self.thumb_name)
        except Exception as e:
            print(e)
