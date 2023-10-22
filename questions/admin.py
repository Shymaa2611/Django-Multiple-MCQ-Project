from django.contrib import admin
from .models import Profile,Chapter,Question,UserResponse

admin.site.register(Profile)
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(UserResponse)
