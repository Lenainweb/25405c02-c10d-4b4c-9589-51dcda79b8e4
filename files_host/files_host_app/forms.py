from django import forms
from django.db import models

from .models import File


class FileForm(forms.ModelForm):
    """ file upload form """

    class Meta:

        model = File
        fields = (            
            "file",
            "permission_for_file",
    )

