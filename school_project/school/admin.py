from django.contrib import admin

from school.models import Student
admin.site.register(Student)

from school.models import Teacher
admin.site.register(Teacher)

from school.models import ClassRoom
admin.site.register(ClassRoom)