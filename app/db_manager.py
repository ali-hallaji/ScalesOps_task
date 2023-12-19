from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, ImageModel
import base64
from io import BytesIO


class DBManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def store_images(self, images):
        session = self.Session()
        try:
            for img in images:
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                img_data = buffer.getvalue()
                img_model = ImageModel(image_data=img_data)
                session.add(img_model)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
