from image_downloader import ImageDownloader
from image_processor import ImageProcessor
from db_manager import DBManager


class MainApp:
    def __init__(self, db_url, google_api_key, google_cse_id):
        # Initialize DBManager and ImageDownloader objects
        self.db_manager = DBManager(db_url)
        self.downloader = ImageDownloader(google_api_key, google_cse_id)

    def run(self, query, max_images):
        # Fetch image URLs using the ImageDownloader object
        image_urls = self.downloader.fetch_image_urls(query, max_images)
        # Download and resize images using the ImageProcessor object
        images = ImageProcessor.download_and_resize_images(image_urls)
        # Store images in the database using the DBManager object
        self.db_manager.store_images(images)


if __name__ == "__main__":
    # Configuration parameters
    DATABASE_URL = "postgresql://user:password@db/mydatabase"
    GOOGLE_API_KEY = "your_google_api_key"
    GOOGLE_CSE_ID = "your_google_cse_id"
    QUERY = "example search query"
    MAX_IMAGES = 10

    # Create MainApp object and run the application
    app = MainApp(DATABASE_URL, GOOGLE_API_KEY, GOOGLE_CSE_ID)
    app.run(QUERY, MAX_IMAGES)
