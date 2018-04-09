from django import forms
from django.contrib.auth.models import User

from .models import (
    GRADES, Student, UnpreparedList, Book, Booking, FinalGrades
)


''' Teacher Section '''


class StudentSearchForm(forms.Form):
    name = forms.CharField(label='Nazwisko ucznia')


class StudentGradesForm(forms.Form):
    grade = forms.ChoiceField(label='Ocena', choices=GRADES)
    evaluation = forms.CharField(max_length=1024)


class FinalGradesForm(forms.ModelForm):
    class Meta:
        model = FinalGrades
        fields = ['half', 'final']


class PresenceListForm(forms.Form):

    student = forms.CharField(label='Student', widget=forms.HiddenInput())
    day = forms.DateField(label='Data', widget=forms.HiddenInput())
    present = forms.NullBooleanField(label='Obecny? ')


class UnpreparedListForm(forms.ModelForm):
    class Meta:
        model = UnpreparedList
        fields = '__all__'


''' Auth Section '''


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Haslo', widget=forms.PasswordInput)


class ChangePassForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput())
    new_pass = forms.CharField(widget=forms.PasswordInput())
    new_pass_2 = forms.CharField(widget=forms.PasswordInput())


''' Library Section '''


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'gender', 'is_borrowed', 'tags', 'authors', 'authors' ]




''' Auditorium  Section '''

class NewBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'