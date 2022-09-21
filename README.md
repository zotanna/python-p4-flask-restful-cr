# Create and Read with Flask-RESTful

## Learning Goals

- Build RESTful APIs that are easy for other developers to understand and use
  in their own applications.

***

## Key Vocab

- **Representational State Transfer (REST)**: a convention for developing
  applications that use HTTP in a consistent, human-readable, machine-readable
  way.
- **Application Programming Interface (API)**: a software application that
  allows two or more software applications to communicate with one another.
  Can be standalone or incorporated into a larger product.
- **HTTP Request Method**: assets of HTTP requests that tell the server which
  actions the client is attempting to perform on the located resource.
- **`GET`**: the most common HTTP request method. Signifies that the client is
  attempting to view the located resource.
- **`POST`**: the second most common HTTP request method. Signifies that the
  client is attempting to submit a form to create a new resource.
- **`PATCH`**: an HTTP request method that signifies that the client is attempting
  to update a resource with new information.
- **`PUT`**: an HTTP request method that signifies that the client is attempting
  to update a resource with new information contained in a complete record.
- **`DELETE`**: an HTTP request method that signifies that the client is
  attempting to delete a resource.

***

## Introduction

Flask as you've learned it is already a great tool for building RESTful APIs,
but it's important to always seek out the best tools for the job. There are
dozens of extensions designed exclusively for use with Flask, and one,
[Flask-RESTful][frest], makes it _very_ easy to build RESTful APIs.

***

## Flask-RESTful Example

Let's take a look at a bare-bones API built with Flask-RESTful:

```py
# example only

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Newsletter(Resource):
    def get(self):
        return {"newsletter": "it's a beautiful 108 out in Austin today"}

api.add_resource(Newsletter, '/newsletters')

if __name__ == '__main__':
    app.run()

```

We can run this app just like any other- with `python app.py` or `flask run`-
then navigate to the client in order to access `Newsletter`'s resources. Since
the data here is returned in such a simple format, we can access it most easily
from the command line with `curl`:

```console
$ curl http://127.0.0.1:5000
# => {"newsletter: "it's a beautiful 108 out in Austin today"}
```

So what's going on here?

### `Api` and `Resource`

Flask-RESTful's `Api` class is the constructor for your RESTful API as a whole.
It is initialized with a Flask application instance and populates with resources
later on. These resources all inherit from the `Resource` class, which includes
conditions for throwing exceptions and base methods for each HTTP method that
explicitly disallow them.

When `Resource` subclasses are added to the `Api` instance with
`add_resource()`, it uses the newly defined HTTP verb instance methods to
determine which routes to create at the provided URL.

`Api` and `Resource` aren't the only classes available to us through
Flask-RESTful, but they're more than enough to get us started.

***

## Creating Records with Flask-RESTful

***

## Conclusion

***

## Resources

- [What RESTful Actually Means](https://codewords.recurse.com/issues/five/what-restful-actually-means)
- [Flask-RESTful][frest]
- [HTTP request methods - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

[frest]: https://flask-restful.readthedocs.io/en/latest/
