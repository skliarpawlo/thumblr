"""Use cases are the *only* entry points of thumblr lib, all parameters should be primitive python types, or DTO's (
data transfer objects)
"""

from django.db.transaction import atomic
from thumblr.caching import cached
from thumblr.dto import ImageMetadata
from thumblr.services.cud import create_image, replace_uploaded_image
from thumblr.services.query import get_image_metadata, get_images_by_spec
from thumblr.services.url import get_image_instance_url


__all__ = ['add_image', 'get_image_url', 'update_image']


@atomic
def add_image(uploaded_file, image_metadata):
    assert isinstance(image_metadata, ImageMetadata)

    image = create_image(uploaded_file, image_metadata)

    return get_image_metadata(image)


@cached
def get_image_url(image_metadata, url_spec):
    """
    `image_file_id`, `file_name` and `size_slug` in image_metadata_spec are required for correct url caching
    """
    assert isinstance(image_metadata, ImageMetadata)

    image_file = get_images_by_spec(image_metadata, one=True)

    return get_image_instance_url(image_file, url_spec)


@atomic
def update_image(new_file, image_metadata):
    """Updates image specified by image_metadata spec with new_file.
       new_file - should be instance of django File
       image_metadata - ImageMetadata
    """
    assert isinstance(image_metadata, ImageMetadata)

    image_file = get_images_by_spec(image_metadata)
    replace_uploaded_image(image_file, new_file)

    return get_image_metadata(image_file)


@atomic
def delete_images(image_metadata):
    """
    Removes all images that meet criteria of `image_metadata`
    """
    image_files = get_images_by_spec(image_metadata)
    for image_file in image_files:
        image_file.delete()


def get_all_images(image_metadata):
    assert isinstance(image_metadata, ImageMetadata)

    image_files = get_images_by_spec(image_metadata)
    return map(get_image_metadata, image_files)
