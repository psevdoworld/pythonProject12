from django.contrib.auth import get_user_model
from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    CharField,
    TextField, ImageField
)
User = get_user_model()
class Post(Model):
    author = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=200)
    text = TextField()
    picture = ImageField(null=True)
    def __str__(self):
        return f"Постик {self.title}"
