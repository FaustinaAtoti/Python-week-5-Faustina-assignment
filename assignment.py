class Book:
    def __init__(self, name, author):
        self.name = name   
        self.author = author
        


book1 = Book("Midnight Clear", "Autumn Macarthur")
book2 = Book("Girl Defined", "Kristen Clark")

print(book1.name)  
print(book2.author)  

# Polymorphism
class Book1:    
    def remark(self):
        return("Wonderful Book.")

class Book2:
    def remark(self):
        return("Best booK Ever!")
    
for book in [Book1(), Book2()]:
    print(book.remark())  
