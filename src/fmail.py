#!/usr/bin/env python3
"""FMail web page and API."""

from falcon import API, HTTP_200, HTTP_500
from tasks.send_email import sendmail
import sys


class SendEmail:
    """FMail API."""
    def on_post(self, req, resp):
        """POST handler for FMail API endpoint."""
        promise = sendmail.delay(req.media['to_addr'], req.media['subject'],
                                 req.media['body'])
        resp.status = HTTP_200 if promise else HTTP_500


APP = API()
APP.add_route('/api', SendEmail())
