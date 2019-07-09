from django.http import HttpResponse
from apipkg import api_manager as api


def index(request):
    app_info = api.send_request('catalogueproduits', 'info')
    return HttpResponse("Je suis Gestion Commerciale et je demande un truc à %r" % app_info)

def info(request):
	return HttpResponse("Gestion Commerciale")