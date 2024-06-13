# Containerized library API
`git clone https://github.com/JaroslawBozek/applover`

## Run App
Go to the folder with Dockerfile

## Option 1: Docker compose
`docker-compose up`

## Option 2: Docker build
### Build a docker image
`docker build -t applover-library .`

### Build and run a container
`docker run -p 3000:3000 applover-library`

## Routes

### GET book list
curl http://localhost:3000/books

### POST a new book
curl -X POST http://localhost:3000/books \
     -H "Content-Type: application/json" \
     -d '{
           "serial_number": "000001",
           "title": "Example Book",
           "author": "Author Name"
         }'

### PATCH existing book's status
curl -X PATCH http://localhost:3000/books/000001  \
     -H "Content-Type: application/json" \
     -d '{"is_borrowed": true, "borrowed_by": "999999"}'
     
### DELETE existing book
curl -X DELETE http://localhost:3000/books/000001
