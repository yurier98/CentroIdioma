import logging

from django.contrib import auth
from django.contrib.auth import logout, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Pagina de inicio
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import RedirectView, FormView

from Convocatorias.models import Convocatoria
from GestionLab.forms import LoginForm, SignUpForm
from GestionLab.models import Materiales

logger = logging.getLogger(__name__)


def homepage(request):
    latest_convocatoria_list = Convocatoria.objects.order_by('-fechaCreada')[:6]
    context = {'latest_convocatoria_list': latest_convocatoria_list}
    return render(request, "index.html",context)


def materiales(request):
    materiales_list = Materiales.objects.all()
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


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = '/'
        kwargs['redirect_to'] = redirect_to

        return super(LoginView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST, request=self.request)

        if form.is_valid():
            #  from DjangoBlog.utils import cache
            #   if cache and cache is not None:
            #       cache.clear()
            logger.info(self.redirect_field_name)

            auth.login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
            # return HttpResponseRedirect('/')
        else:
            return self.render_to_response({
                'form': form
            })

    def get_success_url(self):

        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(
                url=redirect_to, allowed_hosts=[
                    self.request.get_host()]):
            redirect_to = self.success_url
        return redirect_to


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
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "autentications/register.html", {"form": form, "msg": msg, "success": success})