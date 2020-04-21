from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\n E-mail: {email}\n Mensagem: {message}'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br'],
            headers={'Replay-To': email}
        )

        mail.send()