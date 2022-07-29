## Wookie Book Store

A simple bookstore with REST API implementation

### Design & decisions
Here I am creating a store with a custom User model and a simple Book model. The User customization was chosen in order to add special field and make it easier to change the model in further development. Simultaneously Rest Framework allows implementing API faster and make them readable for further usage.

### Enteties

There are two basic entities:
User and Book.

User represent book author and contains:
* name
* email - unique
* author pseudonym
* is_active
* is_staff

Book represents Book and contains:
* title
* description
* author - author_id
* cover image - store in 'book covers'
* price - decimal

### API

There are crucial API for basic needs - Book List/Detail View, Update and Delete. List view allows everyone in read only mode. Add books may all authentificated users. Update and Delete may only author. This type of permission you can find in permissions.py. 

### JWT Authentication
For this tpe of token authentification Simple JWT plugin was used. 

### Tests

Actually it was my first time making tests, do I test the ability to create a book. It is not allowed to unauthenticated users, as mentioned beyond, but works good for authenticated users.
Running the tests will create a test database and populate it with some test data ans then destroy it.

`python manage.py test`


### Blacklist

There is a validation in Book model for author added as a bonus - Darth Vader cannot publish any book. The BLACKLIST list is added to settings.py in order to have ability to add another users in future. 

