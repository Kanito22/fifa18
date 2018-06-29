from django.contrib import admin

from .models import Question, Team


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('teams', {'fields': ['team1', 'team2']}),
        ('scores', {'fields': ['score1', 'score2']}),
    ]

    list_display = ('question_text', 'team1', 'team2', 'pub_date')


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['team_text', 'winner']}),
    ]

    list_display = ('team_text', 'winner')


admin.site.register(Question, QuestionAdmin)

admin.site.register(Team, TeamAdmin)