from django.forms import ModelForm
from parcel.models import Parcel

class ParcelForm(ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'
