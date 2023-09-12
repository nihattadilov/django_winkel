from core.models import Setting

def settings(request):
    context={
        'settings':Setting.objects.first()
    }
    return context