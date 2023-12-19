import requests


class ImageDownloader:
    def __init__(self, api_key, cse_id):
        self.api_key = api_key
        self.cse_id = cse_id
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def fetch_image_urls(self, query, num_images):
        """
        Fetches image URLs from Google Custom Search API using the provided query and number of images.
        Returns a list of image URLs.
        """
        params = {
            'key': self.api_key,
            'cx': self.cse_id,
            'q': query,
            'searchType': 'image',
            'num': num_images
        }

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        results = response.json()
        image_urls = [item['link'] for item in results.get('items', [])]

        return image_urls
