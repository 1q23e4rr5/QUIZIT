from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Question, UserAnswer, QuizSettings

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'hearts', 'total_score', 'date_joined']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'correct_option', 'used_count']
    list_filter = ['correct_option']
    search_fields = ['text']

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'selected_option', 'is_correct', 'created_at']
    list_filter = ['is_correct', 'created_at']

@admin.register(QuizSettings)
class QuizSettingsAdmin(admin.ModelAdmin):
    list_display = ['total_questions', 'points_per_correct', 'points_per_wrong', 'is_active']