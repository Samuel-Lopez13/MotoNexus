from django.utils.deprecation import MiddlewareMixin
from .utils import user_belongs_to_admin_group

#Cree un middleware para saber a que grupo pertenece el usuario
class MiddlewareGroup(MiddlewareMixin):
    def process_request(self, request):
        #La variable debe empezar con el request para reconocer la solicitud
        request.belongs_group = user_belongs_to_admin_group(request.user)