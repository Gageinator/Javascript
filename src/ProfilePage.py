import tornado.web
import random

D = {
    "alice":
    {
        "name" : "Alice Smith",
        "DOB" : "Jan.1",
        "email" : "alice@example.com",
        "image" : "/static/Alice.png"
    },
    "bob":
    {
        "name" : "Bob Jones",
        "DOB" : "Dec.31",
        "email" : "bob@bob.xyz",
        "image" : "/static/Bob.png"
    },
    "carol":
    {
        "name" : "Carol Ling",
        "DOB" : "Jul.17",
        "email" : "carol@example.com",
        "image" : "/static/Carol.png"
    },
    "dave":
    {
        "name" : "Dave N. Port",
        "DOB" : "Mar.14",
        "email" : "dave@dave.dave",
        "image" : "/static/Dave.png"
    }
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        L = self.request.path.split("/")
        uname = L[2]
        info = D[uname]
        self.render("profilepage.html",
                    name=info["name"], dateOfBirth=info["DOB"],
                    email=info["email"], image=info["image"])
        