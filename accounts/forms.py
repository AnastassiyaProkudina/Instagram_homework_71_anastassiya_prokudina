from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-field ", "placeholder": "Эл. адрес"}
        ),
    )
    password = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-field ", "placeholder": "Пароль"}
        ),
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="",
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-field ", "placeholder": "Пароль"}
        ),
    )
    password_confirm = forms.CharField(
        label="",
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-field ", "placeholder": "Повторите пароль"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "avatar",
            "password",
            "password_confirm",
            "first_name",
            "bio",
            "phone",
            "gender",
        )
        username = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Логин"})
        self.fields["username"].help_text = None
        self.fields["email"].widget.attrs.update({"placeholder": "Эл.почта"})
        self.fields["first_name"].widget.attrs.update({"placeholder": "Имя"})
        self.fields["bio"].widget.attrs.update(
            {"placeholder": "Напишите немного о себе"}
        )
        self.fields["phone"].widget.attrs.update({"placeholder": "Телефон"})
        self.fields["gender"].widget.attrs.update({"placeholder": "Пол"})
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-field"
            visible.label = ""

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.groups.add('users')
        if commit:
            user.save()
        return user


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=20,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "search-bx",
                "placeholder": "Поиск",
                "onchange": "submit();",
            }
        ),
    )


class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
        labels = {"first_name": "Имя", "last_name": "Фамилия", "email": "Email"}
