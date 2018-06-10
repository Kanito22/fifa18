from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('teams', {'fields': ['team1', 'team2']}),
        ('scores', {'fields': ['score1', 'score2']}),
    ]

admin.site.register(Question, QuestionAdmin)