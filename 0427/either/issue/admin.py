from django.contrib import admin
from .models import Issue, Reply

# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('nameA', 'nameB', 'hitcountA', 'hitcountB')

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('pick', 'comment', )

admin.site.register(Issue, IssueAdmin)
admin.site.register(Reply, ReplyAdmin)