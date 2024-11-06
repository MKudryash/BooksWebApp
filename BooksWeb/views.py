from .models import Books, Feedback
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .form import FeedbackForm
from django.http import HttpResponseRedirect


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



  
def allbooks(request):
    # получаем все объекты
    books = Books.objects.all()
    print(books.query)
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
 