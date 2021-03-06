from django.contrib import admin
from quiz.models import Question, Answer, Result

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 4

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('text', 'question', 'correct')

class ResultAdmin(admin.ModelAdmin):
	list_display = ('name', 'score', 'date_taken')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)