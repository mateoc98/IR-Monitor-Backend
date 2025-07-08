from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class RatingReport(db.Model):
    __tablename__ = 'rating_reports'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agency = db.Column(db.Text, nullable=False)
    bank_name = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Text)
    outlook = db.Column(db.Text)
    report_date = db.Column(db.DateTime)
    summary = db.Column(db.Text)
    full_report_url = db.Column(db.Text)
