from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactModelForm


def contact(request):
    form = ContactModelForm()
    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'contact.html', {'form': form})
