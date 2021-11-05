from django.db import models
from django.urls import reverse
from django.conf import settings

class File(models.Model):
    """model for file"""

    PERMISSION = [
        ("PRIVAT", "private"),
        ("LINK", "link"),
        ("PUBLIC", "public"),       
    ]

    original_filename = models.CharField("original filename", max_length=50)
    guid_name = models.CharField("Globally Unique Identifier", max_length=40)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/uploads/")
    permission_for_file = models.CharField("permission for file", choices=PERMISSION, default="PRIVAT", max_length=8)
    count_download = models.PositiveIntegerField("count download", default=0)

    def get_absolute_url(self):
        return reverse("file_detail", kwargs={"slug": self.guid_name})
    
    def __str__(self) -> str:
        return self.original_filename
