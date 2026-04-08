from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SuggestionForm


def suggestion_form(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message was received.")
            return redirect('suggestions')
        messages.error(request, "Please fix the errors below.")
    else:
        form = SuggestionForm()
    return render(request, 'suggestions/form.html', {'form': form})
