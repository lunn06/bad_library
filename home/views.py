from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

def home(request):
    if not request.user.is_authenticated:
        return redirect('user/login')
    else:
        return render(request, 'home.html', context={"username": request.user.username})