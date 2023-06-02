from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def index(request):
    objs = Record.objects.all()
    return render(request, 'index.html', context={
        'records':objs,
        'is_authenticated':request.user.is_authenticated
    })

@login_required
def uploadLink(request):
    return HttpResponse('Login Required for Link Upload. You are logged in if you can see this.')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Record

class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    fields = ['title', 'description', 'link']
    success_url = '/'  # Replace with the URL to redirect after successful form submission
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

