books = {
    1:{"title":"Мёртвые души","author":"Николай Гоголь","year":"1842"},
    2:{"title":"Война и мир ","author":"Лев Толстой","year":"1869"},
    3:{"title":"Мастер и Маргарита","author":"Михаил Булгаков","year":"1967"},
    4:{"title":"Преступление и наказание","author":"Фёдор Достоевский","year":"1866"},
    5:{"title":"Маленький принц","author":"Антуан де Сент-Экзюпери","year":"1943"},
}
count = 1
for key,book in books.items():
    print("-"*20,"Книга",count,"-"*20)
    print("Название:",book["title"],end=", ")
    print("Автор: ",book["author"])
    print("-"*20,book['year'],"-"*20)
    count+=1
