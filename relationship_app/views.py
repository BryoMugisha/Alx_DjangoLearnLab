from django.http import HttpResponse
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library


def list_books(request):
    books = Book.objects.select_related('author')

    response_lines = []
    for book in books:
        response_lines.append(f"{book.title} by {book.author.name}")

    return HttpResponse("\n".join(response_lines), content_type="text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context