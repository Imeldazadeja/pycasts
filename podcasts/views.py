from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Episode
# Create your views here.
class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Episode
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Episode.objects.select_related().filter().order_by('-pub_date'), self.paginate_by)
        context["episodes"] =  p.page(context['page_obj'].number)

        return context


