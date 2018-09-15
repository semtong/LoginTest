from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # admin에 보여주고 싶은 칼럼명을 표시한다.
    list_display = ("id", "title", "created_at", "updated_at")


admin.site.register(Post, PostAdmin)