# author = E-RROR <sina.farhadi@protonmail.com>
# how this code works request --> django
# middleware <-- request then check request session based
# on last saved sessions think to block or not
# then return the response
from django.conf import settings
from django.http import HttpResponseForbidden
import json
import datetime

def DjangoMosquito(get_response):
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # -----------------------
        # if we have limit in settings
        # we use that but if we don"t
        # we use 300 as default
        try:
            LIMIT_COUNT = settings.LIMIT_MOSQUITO
        except:
            LIMIT_COUNT = 100

        # check the session first
        if request.session.get("mosquito"):
            # we know that user already visits
            # and have the sessions
            # now we check the times user visits
            # the websites today by timestamp
            # first loads into dict
            parsed_mosquito = json.loads(request.session["mosquito"])
            # now parsed_mosquito is an type of dictionary
            # we can get the objects and data"s in it
            mosquito_time = parsed_mosquito["time"]
            # now we have current_time and mosquito_time
            # we should check that the times are in same day
            if mosquito_time == str(datetime.datetime.today().date()):
                # its in same day
                # now we should only pluses
                # the count number
                parsed_mosquito["count"] = parsed_mosquito["count"] + 1
                # check for limitation
                if parsed_mosquito["count"] + 1 >= LIMIT_COUNT:
                    # user now should limit !
                    return HttpResponseForbidden('Too many Attemps')

                else:
                    # user should not limit now
                    # we just need to update the count
                    parsed_mosquito["count"] = parsed_mosquito["count"] + 1
                    # save it
                    request.session["mosquito"] = json.dumps(parsed_mosquito)
                    response = get_response(request)

            else:
                # its not in same day
                # we should change it to today
                parsed_mosquito["time"] = str(datetime.datetime.today().date())
                parsed_mosquito["count"] = 1
                # then response the user
                response = get_response(request)

        else:
            # its user first time visit
            # we should setup the sessions
            # for them
            try:
                # try to save the sessions
                # mosquito is an session with
                # value of the timestamp of visit
                # time of the session
                mosquito_template = {
                    "time": str(datetime.datetime.today().date()),
                    "count": 0
                }
                # then save it to session
                # as stringified dictionary
                # with stringify it
                try:
                    request.session["mosquito"] = json.dumps(mosquito_template)
                    request.session.save()
                except Exception as exc:
                    pass

                response = get_response(request)

            except Exception as exc:
                # session fails to set
                # user can continue surfs
                response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response

    return middleware
