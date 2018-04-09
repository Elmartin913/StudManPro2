"""smp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from smpapp.views import (
    LPView,
    # teacher
    TeacherStartView,
    TeacherView,
    TeacherProfieView,
    StudentSearchView,
    StudentGradesFormView,
    FinalGradesFormView,
    PresenceListFormView,
    UnpreparedListFormView,
    # student
    StudentView,
    # auth
    LoginView,
    LogoutView,
    ChangePassView,
    signup,
    UserListView,
    # liblary
    LibraryView,
    NewBookFormView,
    BookUpdateView,
    BookDeleteView,
    BookDetailView,
    # auditorium
    RoomsView,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LPView.as_view(), name='lp'),

    # teacher
    path('teacher', TeacherStartView.as_view(), name='teacher_start'),
    path('teacher/<int:pk>', TeacherProfieView.as_view(), name='teacher_profile'),
    path('teacher/search', StudentSearchView.as_view(), name='teacher_search'),
    path('teacher/<int:class_id>/<int:subject_id>', TeacherView.as_view(), name='teacher_class'),
    path('teacher/<int:class_id>/<int:subject_id>/<int:student_id>/grades', StudentGradesFormView.as_view(), name='teacher_edit_grades'),
    path('teacher/<int:class_id>/<int:subject_id>/<int:student_id>/unpr', UnpreparedListFormView.as_view(), name='teacher_edit_unpr'),
    path('teacher/<int:class_id>/<int:subject_id>/<int:student_id>/pres', PresenceListFormView.as_view(), name='teacher_edit_pres'),
    path('teacher/<int:class_id>/<int:subject_id>/<int:student_id>/finalgrades', FinalGradesFormView.as_view(), name='teacher_final_grades'),
    # student
    path('student/<int:student_id>', StudentView.as_view(), name='student_view'),

    # auth
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password_reset/<int:user_id>', ChangePassView.as_view(), name='password_reset'),
    path('signup', signup, name='signup'),
    path('list_users', UserListView.as_view(), name="list_users"),


    # liblary
    path('library', LibraryView.as_view(), name='library'),
    path('book_create', NewBookFormView.as_view(), name='book_create'),
    path('book_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),

    # auditorium
    #path('rooms', RoomsView.as_view(), name='rooms'),
]
