from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Question, Choice, Answer, SubmitAnswer
from django.template import RequestContext, loader
import pygal
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)


def home(request):
    return render(request, 'polls/home.html', {})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def line(request):
	line_chart = pygal.Line()
	line_chart.title = 'Students Evaluation Results'
	line_chart.x_labels = map(str, range(2002, 2013))
	line_chart.add('Q1', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
	line_chart.add('Q2',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
	line_chart.add('Q3',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
	line_chart.add('Q4',  [10, 20 ,10, 3, 33, 55, 23, 14, 42, 4,3,44,4,4,4,4])
	line_chart.render()
	return HttpResponse(line_chart.render())

def about_us(request):
	return render(request, 'polls/About_us.html', {})

def analysis(request):
	if request.method == 'GET':
	    print request.GET
	elif request.method == 'POST':
	    print request.POST
	    questions = Question.objects.all()
	    questions = Answer.objects.all()
	    line_chart = pygal.Line()
	    line_chart.title = 'Students Evaluation Results'
	    line_chart.x_labels = map(str, range(2002, 2013))
	    line_chart.add('Q1', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
	    line_chart.add('Q2',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
	    line_chart.add('Q3',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
	    line_chart.add('Q4',  [10, 20 ,10, 3, 33, 55, 23, 14, 42, 4,3,44,4,4,4,4])
	    line_chart.render()
	    return HttpResponse(line_chart.render())