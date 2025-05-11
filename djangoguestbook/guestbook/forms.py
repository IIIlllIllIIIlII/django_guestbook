from django import forms

class WriteForm(forms.Form):
    nickname = forms.CharField(label="닉네임", max_length=10)
    secretcode = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    content = forms.CharField(label="내용", max_length=100)