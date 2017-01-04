from datetimewidget.widgets import DateTimeWidget
from django import forms

from asuntos.models import AsuntoEvento


class AsuntoEventoForm(forms.ModelForm):
    class Meta:
        model = AsuntoEvento
        fields = '__all__'
        widgets = {
            'fecha_cita_usuario': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
            'fecha_visita_juzgado': DateTimeWidget(attrs={'id': "yourdatetimeid2"}, usel10n=True, bootstrap_version=3)
        }

    def __init__(self, *args, **kwargs):
        super(AsuntoEventoForm, self).__init__(*args, **kwargs)
        # self.fields['asunto'].widget.attrs['disabled'] = 'disabled'
