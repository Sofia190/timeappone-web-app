from django.shortcuts import render, redirect



def start(request):

	return redirect('welcome')



def welcome(request):

        return render(request, 'start_page.html')







































