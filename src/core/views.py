from django.shortcuts import render
from django.db.models import Q
from customuser.models import CustomUser

def home_view(request):
    return render(request, 'core/index.html')

def search_results_view(request):
    context = {}
    query = request.GET.get('q')
    users_list = CustomUser.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    context['users_list'] = users_list
    return render(request, 'core/search_results.html', context)

