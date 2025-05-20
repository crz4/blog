from django.shortcuts import render

# Create your views here.
def main(request):
    return render(
        request,              # так будет всегда
        'mainpage/main.html',  # путь к шаблону
        # здесь будут данные!
    )