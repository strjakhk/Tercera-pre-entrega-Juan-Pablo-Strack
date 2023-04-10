from django import forms

class Registro(forms.Form):
    user_name = forms.CharField(max_length=25)
    user_pass = forms.CharField(widget=forms.PasswordInput())
    user_email = forms.EmailField()


class Post(forms.Form):
    post_author = forms.CharField(max_length=25)
    post_title = forms.CharField(max_length=40)
    post_content = forms.CharField(widget=forms.Textarea(attrs={'rows' : 10, 'cols' : 100}))


class Comentarios(forms.Form):
    comment_author = forms.CharField(max_length=25)
    comment_content = forms.CharField(widget=forms.Textarea(attrs={'rows' : 10, 'cols' : 100}))