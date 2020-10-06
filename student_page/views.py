from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Tutor, Student, SubjectsStruggling, SubjectsTaught


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Student.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


def swiping(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        selected_choice = student.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Tutor.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'student': student,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(swiping.id,)))