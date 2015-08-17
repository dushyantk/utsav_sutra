from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'utsav_sutra_app/index.html', {})
