from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class NewsArticle(db.Model):
    __tablename__ = 'news_articles'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)
    content = db.Column(db.Text)
    source = db.Column(db.Text)
    published_date = db.Column(db.DateTime)
    scraped_date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.Text)
    region = db.Column(db.Text)  # nacional, internacional
    language = db.Column(db.Text)  # es, en
    url = db.Column(db.Text)
    priority = db.Column(db.Text)  # high, medium, low
    meta_data = db.Column(db.JSON)
