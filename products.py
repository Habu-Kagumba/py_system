import webapp2


class MainHandler(webapp2.RequestHandler):

    """ Receive JSON with product details from HTTP request. """

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Default page')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
