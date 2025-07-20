from datetime import datetime, timezone

from . import db


class Opinion(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    title = db.Column(
        db.String(128),
        nullable=False
        )
    text = db.Column(
        db.Text,
        unique=True,
        nullable=False
        )
    source = db.Column(db.String(256))
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now(timezone.utc)
        )
    added_by = db.Column(db.String(64))

    def to_dict(opinion):
        return dict(
            id=opinion.id,
            title=opinion.title,
            text=opinion.text,
            source=opinion.source,
            timestamp=opinion.timestamp,
            added_by=opinion.added_by
        )

    def from_dict(self, data):
        for field in ['title', 'text', 'source', 'added_by']:
            if field in data:
                setattr(self, field, data[field])
