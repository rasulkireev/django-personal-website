from django import template

register = template.Library()

from books.models import Book

@register.inclusion_tag('template_tags/book_list.html')
def latest_books(book):
  book = Book.objects.filter(status="READ").order_by('-date_read')[0:5]
  return {'book': book}
