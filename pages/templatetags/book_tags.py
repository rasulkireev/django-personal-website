from django import template

register = template.Library()

from books.models import Book

@register.inclusion_tag('template_tags/book_list.html')
def latest_books(book):
  book = Book.objects.filter(draft=False).order_by('-date_read')[0:4]
  return {'book': book}
