from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):

    location = settings.MEDIAFILES_LOCATION




# class CachedS3BotoStorage(S3Boto3Storage):
#     """
#     S3 storage backend that saves the files locally, too.

#     It's needed for static files and django-compressor to get along :)
#     """
#     def __init__(self, *args, **kwargs):
#         super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
#         self.local_storage = get_storage_class(
#             "compressor.storage.CompressorFileStorage")()

#     def save(self, name, content):
#         """Save both on S3 and locally."""
#         name = super(CachedS3BotoStorage, self).save(name, content)
#         self.local_storage._save(name, content)
#         return name

#     def path(self, name):
#         """
#         Return absolute path as saved in local stoarge backend.

#         Required by django-inlinecss.
#         """
#         return self.local_storage.path(name)
