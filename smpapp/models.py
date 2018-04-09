from django.db import models
from django.contrib.auth.models import User

# Create your models here.



''' ------------------- SCHOOL SECTION ------------------- '''

SCHOOL_CLASS = (
    (1, "1 klasa"),
    (2, "2 klasa"),
    (3, "3 klasa"),
)

GRADES = (
    (1, "1"),
    (1.5, "1+"),
    (1.75, "2-"),
    (2, "2"),
    (2.5, "2+"),
    (2.75, "3-"),
    (3, "3"),
    (3.5, "3+"),
    (3.75, "4-"),
    (4, "4"),
    (4.5, "4+"),
    (4.75, "5-"),
    (5, "5"),
    (5.5, "5+"),
    (5.75, "6-"),
    (6, "6")
)


class Student(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Imię')
    last_name = models.CharField(max_length=64, verbose_name='Nazwisko')
    school_class = models.IntegerField(choices=SCHOOL_CLASS, verbose_name='Klasa')
    email = models.EmailField(verbose_name='Email', blank=True)
    suspended = models.BooleanField(default=True, verbose_name='Aktywny')
    add_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='Aktywny')


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Studenci'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Imię')
    last_name = models.CharField(max_length=64, verbose_name='Nazwisko')
    email = models.EmailField(verbose_name='Email', blank=True)
    suspended = models.BooleanField(default=True, verbose_name='Aktywny')
    add_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='Aktywny')
    #rozbudowa użytkownika przez nadpisanie modelu

    class Meta:
        verbose_name = 'Nauczyciel'
        verbose_name_plural = 'Nauczyciele'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class SchoolSubject(models.Model):
    name = models.CharField(max_length=64, verbose_name='Przedmiot')
    # relationships: teacher
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='schoolsubject')

    class Meta:
        verbose_name = 'Przedmiot'
        verbose_name_plural = 'Przedmioty'

    def __str__(self):
        return self.name


class StudentGrades(models.Model):
    grade = models.FloatField(choices=GRADES)
    avg = models.FloatField(default=0)
    evaluation = models.TextField(null=True, default='NT')
    # relationships:
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='studentGrades')
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE, related_name='studentGrades')

class FinalGrades(models.Model):
    avg1 = models.FloatField(default=0)
    avg2 = models.FloatField(default=0)
    half = models.FloatField(choices=GRADES, blank=True, null=True, default=0)
    final = models.FloatField(choices=GRADES, blank=True, null=True, default=0)
    # relationships:
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='finalGrades')
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE, related_name='finalGrades')


class PresenceList(models.Model):
    day = models.DateField()
    present = models.NullBooleanField()
    # relationships:
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE, null=True)


class UnpreparedList(models.Model):
    unprep_one_used = models.BooleanField(default=False)
    unprep_two_used = models.BooleanField(default=False)
    # relationships:
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE)


''' ------------------- LIBRARY SECTION ------------------- '''

GENRES = (
    (1, 'podręczniki'),
    (2, 'prace naukowe'),
    (3, 'magazyny naukowe'),
    (4, 'ćwiczenia'),
    (5, 'vademecum'),
)


class Author(models.Model):
    first_name = models.CharField(max_length=256, verbose_name='Imie', null=True)
    last_name = models.CharField(max_length=256, verbose_name='Nazwisko', null=True)
    #books2

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256, verbose_name='Tytul', null=True)
    gender = models.IntegerField(choices=GENRES, verbose_name='Gatunek', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_borrowed = models.NullBooleanField(default=False, verbose_name='Wypożyczona?')
    date_added = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='books')  # 'Tag' bo klasa tag jest nizej
    authors = models.ManyToManyField(Author, related_name='books2')

    class Meta:
        verbose_name = 'Książka'
        verbose_name_plural = 'Książki'

    def name2(self):
        return '{}'.format(self.title)

    def __str__(self):
        return self.name2


class Tag(models.Model):
    tag_name = models.CharField(null=True, max_length=256, verbose_name='Tag')
    # books

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'

    def __str__(self):
        return self.tag_name

    def books_string(self):
        titles = [book.title for book in self.books.all()]
        return ', '.join(titles)


''' Auditorium Section '''

PROJECTOR_STATUS = (
    (1, 'projektor'),
    (2, 'brak projektora')
)


class Auditorium(models.Model):

    name = models.CharField(max_length=64)
    capacity = models.IntegerField(null=True)
    description = models.TextField(null=True)
    projector = models.IntegerField(choices=PROJECTOR_STATUS, null=True)

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aule'

    def __str__(self):
        return self.name


class Booking(models.Model):
    date = models.DateField(null=True)
    auditorium = models.ForeignKey(Auditorium, null=True, related_name='room', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, related_name='teacher', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
