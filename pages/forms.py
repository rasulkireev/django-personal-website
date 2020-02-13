from django.forms import ModelForm
from newsletter.models import Email

class NewsletterSignupHomeForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super(NewsletterSignupHomeForm, self).__init__(*args, **kwargs)
            
            for fieldname in ['user_email']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'w-full p-1 leading-tight text-gray-800 bg-gray-100 border rounded appearance-none focus:outline-none focus:bg-white '})

    class Meta:
        model = Email
        fields = ('user_email',)