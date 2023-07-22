from .models import Employee
from django import forms


class EmForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["eid", "ename", "eage", "edesgn", "eexprev"]
        widgets = {
            "eid": forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Employee Id",
                }
            ),
            "ename": forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Employee name",
                }
            ),
            "eage": forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Employee age",
                    "max": 70,
                    "min": 19,
                }
            ),
            "edesgn": forms.Select(
                attrs={
                    "class": "form-control my-2",
                }
            ),
            "eexprev": forms.Textarea(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "enter Review",
                    "rows": 3,
                }
            ),
        }
