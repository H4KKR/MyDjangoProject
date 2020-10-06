from django.contrib import admin
from .models import Tutor, SubjectsTaught, Student, SubjectsStruggling

# Register your models here.
admin.site.register(Tutor)
admin.site.register(SubjectsTaught)

admin.site.register(Student)
admin.site.register(SubjectsStruggling)