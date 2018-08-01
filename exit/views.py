from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views import generic, View


class IndexView(View):

	def get(self, request):
		return render_to_response('exit/exit.html')
