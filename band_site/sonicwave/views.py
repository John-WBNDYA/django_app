from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Album 


# Create your views here.
class MyLoginView(LoginView):
    """
    This class is used to handle user login.
    It requires the user to provide a valid username and password.
    The user is then redirected to the home page.
    """
    template_name = 'login.html'


@login_required
def home(request):
    """This view renders the home page of the website.
    It requires the user to be logged in and displays a navigation bar
    with links to the band's about page and album page. The home page
    also displays a Sonicwave logo and a background image of a sound
    wave. The background image is a linear gradient."""

    return render(request, 'home.html')


def about(request):
    """This view renders the about page of the website.
    It displays information about the band including its history, members
    and influences."""
    return render(request, 'about.html')

def albums(request):
    """This view renders the albums page of the website.
    It displays a list of the band's albums with a link to the information
    page of each album."""
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})