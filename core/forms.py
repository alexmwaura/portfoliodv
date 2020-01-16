from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'id': 'name',
        'data':{'name'},
        'data-rule':"minlen:4", 
        'data-msg':"Please enter at least 4 chars",
        'class':'form-control'
    }))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Your Email',
        'id': 'email',
        'data':{'from_email'},

        'data-rule':"email",
        'data-msg':"Please enter a valid email",
        'class':'form-control'

    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'data':{'subject'},

        'id': 'subject',
        'data-rule':"minlen:4",
        'data-msg':"Please enter at least 8 chars of subject",
        'class':'form-control'

    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Please Write Something...',
        'data':{'message'},

        'name': 'message',
        'data-rule':"required",
        'data-msg':"Please write something for us",
        'class':'form-control'


    })) 
 

