from django.http import HttpResponse
from django.views import View


class BooksView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Library Books Page!")
