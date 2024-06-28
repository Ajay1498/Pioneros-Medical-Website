from .models import *
def header(request):
    return {'header': Header.objects.first(), 'services': Products.objects.all(), 'headers': Header.objects.all()}