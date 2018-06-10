from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
from users.models import CustomUser


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        #return Question.objects.filter(
        #    pub_date__lte=timezone.now()
        #).order_by('-pub_date')[:5]
        return Question.objects.all().order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_entries = Choice.objects.filter(user_id=self.request.user.id)
        total_sum = 0
        for entry in all_entries:
            total_sum += entry.get_score()

        context['number'] = total_sum
        return context

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        #return Question.objects.filter(pub_date__lte=timezone.now())
        return Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_entries = Choice.objects.filter(user_id=self.request.user.id, question_id=context['question'].id)

        context['all_entries'] = all_entries

        entries = Choice.objects.filter(question_id=context['question'].id)
        
        d = {}
        for entry in entries:
            user = CustomUser.objects.get(id=entry.user.id)
            d[user.username] = '%s-%s' % (entry.score1, entry.score2)
        
        print(d)

        context['d'] = d

        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    current_user = request.user
    question = get_object_or_404(Question, pk=question_id)
    if question.has_started():
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "No puedes apostar a un partido que ya ha comenzado.",
        })
    try:
        selected_choice = question.choice_set.get(user_id=current_user.id)
    except (KeyError, Choice.DoesNotExist):
        selected_choice = question.choice_set.create(user_id=current_user.id)
        # Redisplay the question voting form.
        #return render(request, 'polls/detail.html', {
        #    'question': question,
        #    'error_message': "You didn't select a choice.",
        #})
    #else:
    # selected_choice.votes += 1
    selected_choice.score1 = request.POST['score1']
    selected_choice.score2 = request.POST['score2']
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:index'))