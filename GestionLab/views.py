import logging

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
# Pagina de inicio
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import RedirectView

from Convocatorias.models import Convocatoria
from GestionLab.forms import LoginForm, SignUpForm
from GestionLab.models import Material

logger = logging.getLogger(__name__)


def homepage(request):
    latest_convocatoria_list = Convocatoria.objects.order_by('-fechaCreada')[:6]
    context = {'latest_convocatoria_list': latest_convocatoria_list}
    return render(request, "index.html",context)


def materiales(request):
    materiales_list = Material.objects.all()
    context = {'materiales_list': materiales_list}
    return render(request, "materiales/materiales_lindex.html", context)


class LogoutView(RedirectView):
    url = '/login/'

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # from DjangoBlog.utils import cache
        #         # cache.clear()
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)



def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Credenciales inválidas'
        else:
            msg = 'Error al validar el formulario'

    return render(request, "autentications/login.html", {"form": form, "msg": msg})

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created'
            success = True

            # return redirect("/login/")

        else:
            msg = 'El formulario no es valido'
    else:
        form = SignUpForm()

    return render(request, "autentications/register.html", {"form": form, "msg": msg, "success": success})