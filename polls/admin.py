from django.contrib import admin

# Register your models here.
from polls.models import Choice, Question, Answer, SubmitAnswer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    inlines = [AnswerInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(SubmitAnswer)
