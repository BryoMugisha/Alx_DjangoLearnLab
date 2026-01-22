# Create
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Book: Book object (1)

# Retrieve
book = Book.objects.get(id=1)

# Update
book.title = "Nineteen Eighty-Four"
book.save()

Nineteen Eighty-Four 

# Delete
book = Book.objects.get(id=1)
book.delete()
