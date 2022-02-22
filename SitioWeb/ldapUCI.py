import ldap
from django.contrib.auth.models import User

from GestionLab.models import Perfil


class LDAPBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        # Direccion del servidor ldap
        self.servidor_ldap = 'ldap://10.0.0.3'
        # Usuario para inicializar
        self.dn_ldap = 'cn=ad search, ou=Systems, ou=UCI Domain Impersonals, dc=uci, dc=cu'
        # Clave del usuario a inicializar
        self.clave_ldap = 'uF2SODWAHiW0eJboFFQEAvVzJ'
        # CN de los usuarios en el ldap
        self.CONTEXTO = 'OU=uci domain users,DC=uci,DC=cu'
        # Atributos de los usuarios en el ldap
        self.ATRIBUTOS_USUARIO_LDAP = 'samaccountname'
        self.DN_NOMBRE_USUARIO_LDAP = 'givenname'
        self.DN_APELLIDO_USUARIO_LDAP = 'sn'
        self.DN_SOLAPIN_USUARIO_LDAP = 'postofficebox'
        self.DN_CORREO_USUARIO_LDAP = 'mail'
        self.DN_OCUPACION_USUARIO_LDAP = 'title'
        self.DN_FACULTAD = 'department'
        self.DN_FOTO_LDAP = 'thumbnailphoto'
        self.DN_LOGON_COUNT = 'logoncount'

        self.conexion = None
        self.autenticadoDatos = None

        # listado con los atributos
        self.DATOS_USUARIO_LDAP = [
            self.DN_NOMBRE_USUARIO_LDAP,
            self.DN_SOLAPIN_USUARIO_LDAP,
            self.DN_APELLIDO_USUARIO_LDAP,
            self.DN_CORREO_USUARIO_LDAP,
            self.DN_FOTO_LDAP,
            self.DN_OCUPACION_USUARIO_LDAP,
            self.DN_FACULTAD,
            self.DN_LOGON_COUNT,

        ]
        # Establecer la coneccion inicial
        """Intenta conectarce con el usuario y clave para iniciar la coneccion"""
        try:
            self.conexion = ldap.initialize(self.servidor_ldap)

            self.conexion.protocol_version = ldap.VERSION3
            self.conexion.referrals = ldap.OPT_REFERRALS
            resultado = self.conexion.simple_bind_s(self.dn_ldap, self.clave_ldap)

            """Intenta autenticar un usuario cualquiera con su clave en el servidor ldap, devuelve el usuario de ser correcto los datos"""
            if username != None and password != '':
                try:
                    ent = self.Obtener_Resultado(username)
                except:
                    return None
                if ent[0]:
                    try:
                        acceso = self.conexion.simple_bind_s(ent[0], password)
                        if acceso:
                            try:
                                usuario = User.objects.get(username__exact=username)
                                usuario.set_password(password)
                                usuario.save()
                            except:
                                self.autenticadoDatos = ent[1]
                                print(self.autenticadoDatos)
                                usuario = User.objects.create_user(username, self.getCorreo(), password)
                                usuario.is_staff = None
                                perfil = Perfil(user=usuario, solapin=self.getSolapin(), nombre=self.getNombre(),
                                                apellidos=self.getApellidos(), categoria=self.getCategoria(),
                                                area=self.getArea(), foto=self.getFoto())
                                perfil.save()
                                usuario.save()
                        return usuario
                    except:
                        pass
            return None
        except:
            return None

    def Obtener_Resultado(self, usuario):
        """Dado un nombre de usuario, devuelve todos sus datos y su cn"""
        if self.conexion != None:
            try:
                resultado_busqueda = self.conexion.search_s(self.CONTEXTO, ldap.SCOPE_SUBTREE,
                                                            'samaccountname=' + usuario, self.DATOS_USUARIO_LDAP)
                return resultado_busqueda[0]
            except:
                pass
        return [False, False]

    def busquedaAuto(f):
        def wrapper(*arg):
            if len(arg) == 1:
                return f(arg[0], arg[0].autenticadoDatos)
            else:
                return f(arg[0], arg[1])

        return wrapper

    @busquedaAuto
    def getSolapin(self, busqueda):
        if busqueda:
            return busqueda['postOfficeBox'][0]
        return False

    @busquedaAuto
    def getApellidos(self, busqueda):
        if busqueda:
            return busqueda['sn'][0]
        return False

    @busquedaAuto
    def getNombre(self, busqueda):
        if busqueda:
            return busqueda['givenName'][0]
        return False

    @busquedaAuto
    def getCorreo(self, busqueda):
        if busqueda:
            return busqueda['mail'][0]
        return False

    @busquedaAuto
    def getCategoria(self, busqueda):
        if busqueda:
            return busqueda['title'][0]
        return False

    @busquedaAuto
    def getArea(self, busqueda):
        if busqueda:
            return busqueda['department'][0]
        return False

    @busquedaAuto
    def getFoto(self, busqueda):
        if busqueda:
            foto = "http://directorio.uci.cu/sites/all/modules/custom/directorio_de_personas/display_foto.php?id=" + self.getSolapin(
                busqueda)
            return foto
        return False

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
