from google.appengine.api import mail
import webapp2
import requests


default_page = """
<html>
  <body>
    <div>
        <h1>Click button to retrieve products.</h1>
    </div>
    <div>
    <form action="/upload" method="post">
      <div><input type="submit" value="Upload Products"></div>
    </form>
    </div>
  </body>
</html>
"""


class receiveRequest(object):

    """Receive products in JSON from HTTP request.

        Attributes:
            url: A url string pointing to the JSON.
    """

    def __init__(self, url):
        """Return the url endpoint. """
        self.url = url

    @staticmethod
    def endpoint(url):
        """HTTP endpoint to recieve requests."""
        ep = requests.get(url)
        data = ep.json()
        return data

    @staticmethod
    def sendError(email, error):
        """Send error to email in JSON body"""
        msg = mail.EmailMessage(sender='habukagumba@gmail.com',
                                subject='Subject line here')
        # email from failed test
        msg.to = email
        msg.body = """
        Error: %s
        """ % error
        msg.send()

    @classmethod
    def testProducts(cls, url):
        """Test inbound products"""
        products = cls.endpoint(url)
        # Collect all revelant data and validate (write tests)
        # product description super-simple example
        if products['product']['description'] is None:
            error = 'Description not included!'
            email = products['email']
            return cls.sendError(email, error)

    def main(self):
        """Run application"""
        return self.testProducts(self.url)


class MainHandler(webapp2.RequestHandler):

    """ Receive JSON with product details from HTTP request. """

    def get(self):
        self.response.write(default_page)


class ProductHandler(webapp2.RequestHandler):

    """Handle HTTP endpoint to recieve JSON of products. """

    def post(self):
        receiveRequest(
            'http://s3-us-west-2.amazonaws.com/hshtmlemail/products.json'
        ).main()
        self.response.write('Data processed')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/upload', ProductHandler)
], debug=True)
