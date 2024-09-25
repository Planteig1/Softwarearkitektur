# Members API

This is a simple Flask API for managing members, providing endpoints to retrieve, create, update, and delete members.

## API Endpoints

## 1 - /members [GET]
Shows all the members of the api, and if provided with an apikey - shows public and private repositories for each member

## 2 -/members [POST]
Used to create a new member in the database
Needs to be provided with a "Member" through the https request 
Example: {
  "first_name": "Sophie",
  "last_name": "Anderson",
  "birth_date": "1992-05-16",
  "email": "sophie.anderson92@example.com",
  "phonenumber": "+1-555-987-6543",
  "address": "123 Elm Street, Springfield, IL, USA",
  "nationality": "American",
  "active": true,
  "github_username": "sophieAnders92"
}


## 3 -/members [PUT]
Used to update an already existing members github username
Needs to be provided with
* New github username
* ID - on the member youre trying to edit

## 4 -/members [DELETE]
Used to delete a member from the database
Needs to be provided with
* ID - on the member youre trying to delte from the database


### MISSING
* Error handling - What happens if the request is bad, something goes wrong with the database etc...

* Correct response status codes for each endpoint


