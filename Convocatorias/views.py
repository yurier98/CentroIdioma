from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
from Convocatorias.models import Convocatoria


class ConvocatoriaListView(ListView):
    template_name = 'convocatorias/convocatorias_index.html'
    context_object_name = 'convocatoria_list'
    page_type = ''
    paginate_by = settings.PAGINATE_BY




    @property
    def page_number(self):
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(
            page_kwarg) or self.request.GET.get(page_kwarg) or 1
        return page

    def get_context_data(self, **kwargs):
        kwargs['linktype'] = self.link_type
        return super(ConvocatoriaListView, self).get_context_data(**kwargs)


class IndexView(ConvocatoriaListView):

    def get_queryset_data(self):
        convocatorias_list = Convocatoria.objects.filter(estado='P')
        return convocatorias_list

    def get_queryset_cache_key(self):
        cache_key = 'index_{page}'.format(page=self.page_number)
        return cache_key



def index(request):
  #  latest_convocatoria_list = Convocatoria.objects.order_by('-fechaCreada')[:5].filter(estado='P')
    latest_convocatoria_list = Convocatoria.objects.filter(estado='P')
    context = {'latest_convocatoria_list': latest_convocatoria_list}
    return render(request, 'convocatorias/convocatorias_index.html', context)

def convocatoria_detail(request, id):
    convocatoria = get_object_or_404(Convocatoria, pk=id)
    return render(request, 'convocatorias/convocatorias_detail.html', {'convocatoria': convocatoria})