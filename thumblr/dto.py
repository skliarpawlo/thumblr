__all__ = ['ImageMetadata', 'ImageUrlSpec']


class ImageMetadata(object):
    def __init__(self,
                 image_file_id=None,
                 image_hash=None,

                 file_name=None,
                 site_id=None,
                 size_slug=None,
                 content_type_id=None,
                 object_id=None):
        self.image_file_id = image_file_id
        self.image_hash = image_hash

        self.original_file_name = file_name
        self.site_id = site_id
        self.content_type_id = content_type_id
        self.object_id = object_id
        self.size_slug = size_slug

    def __str__(self):
        return "{image_file_id}::{file_name}::{size}::{site_id}::{content_type}::{object_id}".format(
            image_file_id=self.image_file_id,
            file_name=self.original_file_name,
            size=self.size_slug,
            site_id=self.site_id,
            content_type=self.content_type_id,
            object_id=self.object_id,
        )


class ImageUrlSpec(object):
    S3_URL = 's3'
    CDN_URL = 'cdn'
    PATH_ONLY_URL = 'path'