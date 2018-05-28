import datetime

from django.db import models
from django.utils import timezone


class Team(models.Model):
    team_text = models.CharField(max_length=200)

    def __str__(self):
        return self.team_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    score1 = models.IntegerField(null=True)
    score2 = models.IntegerField(null=True)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1', default=1)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2', default=1)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

    def get_score(self):
        diff1 = self.question.score1 - self.score1
        diff2 = self.question.score2 - self.score2

        if diff1 == 0 and diff2 == 0:
            return 2 # perfect!
        elif ((diff1 == diff2) or
                (self.score1 > self.score2 and
                self.question.score1 > self.question.score2) or
                (self.score1 < self.score2 and
                self.question.score1 < self.question.score2)):
            return 1 # great!
        else:
            return 0 # sorry :(

    def __str__(self):
        return self.choice_text