from django.contrib import admin

from .models import Question, Team


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('teams', {'fields': ['team1', 'team2']}),
        ('scores', {'fields': ['score1', 'score2']}),
        ('scores_final', {'fields': ['score1_final', 'score2_final']}),
    ]

    list_display = ('has_results', 'team1', 'team2', 'pub_date', 'question_text')


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['team_text', 'winner']}),
    ]

    list_display = ('team_text', 'winner')


admin.site.register(Question, QuestionAdmin)

admin.site.register(Team, TeamAdmin)