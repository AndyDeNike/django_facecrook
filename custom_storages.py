from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):

    location = settings.MEDIAFILES_LOCATION




# class CachedS3BotoStorage(S3Boto3Storage):
#     """
#     S3 storage backend that saves the files both remotely and locally.

#     See http://django_compressor.readthedocs.org/en/latest/remote-storages/
#     """
#     def __init__(self, *args, **kwargs):
#         super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
#         self.local_storage = get_storage_class(
#             "django.core.files.storage.FileSystemStorage")()

#     def save(self, name, content):
#         name = super(CachedS3BotoStorage, self).save(name, content)
#         self.local_storage._save(name, content)
#         return name