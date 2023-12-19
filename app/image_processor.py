from PIL import Image  # import the Image module from the PIL library
import requests
from io import BytesIO  # import the BytesIO module from the io library


class ImageProcessor:
    @staticmethod
    def download_and_resize_images(image_urls, size=(100, 100)):
        """
        This method downloads images from a list of URLs and resizes them to a specified size.

        Args:
            image_urls (list): A list of URLs to download images from.
            size (tuple): A tuple representing the desired size of the images. Defaults to (100, 100).

        Returns:
            list: A list of resized images.
        """
        resized_images = []  # create an empty list to store the resized images
        for url in image_urls:  # iterate over each URL in the list of image URLs
            response = requests.get(url,timeout=30)  # send a GET request to the URL and store the response
            img = Image.open(BytesIO(response.content))  # open the image from the response content using the Image module
            resized = img.resize(size)  # resize the image to the specified size
            resized_images.append(resized)  # add the resized image to the list of resized images
        return resized_images  # return the list of resized images
