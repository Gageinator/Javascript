import asyncio
import os, os.path
import tornado.web
import Index, ProfilePage

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)

def makeApp():
    endpoints=[
        ("/",Index.Handler),
        ("/name",ProfilePage.ProfileHandler),
        ("/profile/.*",ProfilePage.ProfileHandler) 
    ]
    app = tornado.web.Application(
        endpoints,
        static_path=HTMLDIR
    )
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()