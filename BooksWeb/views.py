from .models import Books, Feedback
from django.shortcuts import render, get_object_or_404
from .form import FeedbackForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse

# получаем все объекты
books = Books.objects.all()
print(books.query)

# получаем объекты с именем Jane Eyre
books = books.filter(title = "Jane Eyre")
print(books.query)
 
# получаем объекты с годом выпуска, равным 1900
books = books.filter(yearPublish = 1900)
print(books.query)
 
# здесь происходит выполнения запроса в БД
for book in books:
    print(f"{book.id}.{book.title} - {book.author}")

def filter_books(request):
    title = request.GET.get('title')
    author = request.GET.get('author')
    year = request.GET.get('year')

    books = Books.objects.all() # Replace with your actual filter logic

    if title:
        books = books.filter(title__icontains=title)
    if author:
        books = books.filter(author__icontains=author)
    if year:
        books = books.filter(year=year)

    book_data = [{
        'id': book.id, 
        'title':book.title,
        'author': book.author,
        'year': book.year,
        'image': book.image.url # Assuming you have an image field
    } for book in books]

    return JsonResponse(book_data, safe=False)


  
def allbooks(request):
    # получаем все объекты
    books = Books.objects.all()
    print(books.query)

     # Фильтрация по названию книги
    title_query = request.GET.get('title')
    if title_query:
        books = books.filter(title__icontains=title_query)

    # Фильтрация по автору
    author_query = request.GET.get('author')
    if author_query:
        books = books.filter(author__icontains=author_query)

    # Фильтрация по году
    year_query = request.GET.get('year')
    if year_query:
        books = books.filter(yearPublish=year_query)

    # Сортировка
    sort_by = request.GET.get('sort-by')
    if sort_by in ['title', 'author', 'year']:
        books = books.order_by(sort_by)  # Сортируем по выбранному полю
    return render(request, "allbooks.html", {'books':books})

def detailbook(request,id_book:int):
    # получаем объект
    book = get_object_or_404(Books, id = id_book)
    return render(request, "detailbook.html", {'book':book})

def feedbackbook(request,id_book:int):
    # получаем объект
    book = get_object_or_404(Books, id = id_book)
    book_title = book.title

    if request.method == 'POST':
        print('POST')
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed=Feedback(
                nameUser=form.cleaned_data['nameUser'],
                title=book_title,
                email=form.cleaned_data['email'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating']
            )
            feed.save()
            return HttpResponseRedirect('/')
    else:
         form = FeedbackForm(
             initial= {'title': book_title}
              )
    return render(request, "feedbackbook.html", {'book':book, 'form':form})
 