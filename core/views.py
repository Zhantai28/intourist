from django.shortcuts import redirect, render
from django.views import generic, View


class HomeView(generic.TemplateView):
    template_name = "core/index.html"


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile_object = user.profile
        return render(request, 'core/profile.html', {'profile': profile_object})
    else:
        return redirect("core:homepage")
