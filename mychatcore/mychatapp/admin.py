from django.contrib import admin
from .models import(ChatHistory)
from unfold.admin import ModelAdmin
# Register your models here.

@admin.register(ChatHistory)
class ChatHistoryAdmin(ModelAdmin) :
    list_display=("user","question","answer","created_at")