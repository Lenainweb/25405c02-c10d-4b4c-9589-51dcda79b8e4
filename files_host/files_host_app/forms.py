from django import forms
from django.db import models
from .models import File


class FileForm(forms.ModelForm):
    """ file upload form """

    models = File
    fields = (
        "original_filename",
        "file",
        "permission_for_file",
)

