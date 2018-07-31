from .models import Entry
from django.forms import ModelForm


class EventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Entry
        fields = ['name', 'user', 'date', 'time',
                  'description', 'place', 'tags']
