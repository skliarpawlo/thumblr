from copy import deepcopy

__all__ = ['ImageMetadata', 'ImageUrlSpec']


class ImageMetadata(object):
    """
    This should be used everywhere, it abstracts data model. In perfect world, orm models like
    Image and ImageFile should never go out of thumblr application and appear anywhere else.
    """

    def __init__(self,
                 image_file_id=None,
                 image_hash=None,

                 file_name=None,
                 site_id=None,
                 size_slug=None,
                 content_type_id=None,
                 object_id=None,
                 is_main=None,
                 ):
        self.image_file_id = image_file_id
        self.image_hash = image_hash

        self.original_file_name = file_name
        self.site_id = site_id
        self.content_type_id = content_type_id
        self.object_id = object_id
        self.size_slug = size_slug
        self.is_main = is_main

        # for filtering
        self.inverse = False

    def __str__(self):
        return "{image_file_id}::{file_name}::{size}".format(
            image_file_id=self.image_file_id,
            file_name=self.original_file_name,
            size=self.size_slug,
        )

    def invert(self):
        """
        This would revers selection inside fixed content_type_id and object_id. So you *must* specify content_type_id
        and object_id
        """

        assert not self.content_type_id is None, "Inverting dto without content_type_id is UNSAFE"
        assert not self.object_id is None, "Inverting dto without object_id is UNSAFE"

        return self.extend(inverse=not self.inverse)

    def extend(self, **kwargs):
        cpy = deepcopy(self)
        for k, v in kwargs.items():
            if hasattr(cpy, k):
                setattr(cpy, k, v)
        return cpy

    def is_empty(self):
        return \
            self.image_file_id is None and \
            self.original_file_name is None and \
            self.site_id is None and \
            self.content_type_id is None and \
            self.object_id is None and \
            self.image_hash is None and \
            self.is_main is None and \
            self.size_slug is None


class ImageUrlSpec(object):
    S3_URL = 's3'
    CDN_URL = 'cdn'
    PATH_ONLY_URL = 'path'