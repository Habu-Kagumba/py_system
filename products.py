import webapp2


default_page = """
<html>
  <body>
    <form action="/upload" method="post">
      <div><input type="submit" value="Upload Products"></div>
    </form>
  </body>
</html>
"""


class MainHandler(webapp2.RequestHandler):

    """ Receive JSON with product details from HTTP request. """

    def get(self):
        self.response.write(default_page)


class ProductHandler(webapp2.RequestHandler):

    """Handle HTTP endpoint to recieve JSON of products. """

    def post(self):
        self.response.write('Ze outcome')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/upload', ProductHandler)
], debug=True)
