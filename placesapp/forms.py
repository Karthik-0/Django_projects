from .models import Place
from django.forms import ModelForm


class PlaceForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Place
        fields = ['title', 'location', 'desc', 'address', 'phone', 'city',
                  'tags', 'placetypes']
