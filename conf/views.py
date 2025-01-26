from django.shortcuts import render


def handler4045(request, exception):
    return render(request, 'error_page.html')
