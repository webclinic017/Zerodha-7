from django.shortcuts import HttpResponseRedirect
from django.urls import resolve

# if user login then user unable to go back in login page
def login_register_middleware(get_response):
    def middleware(request):
        url_name = resolve(request.path_info).url_name              # resolve convert current path into the name given in urls.py
        if (url_name == 'login_view') and request.user.is_authenticated:
            response = HttpResponseRedirect('home')
        else:
            response = get_response(request)
        return response
    return middleware

# # same function in class
# class Simplemiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         url_name = resolve(request.path_info).url_name
#         if (url_name == 'login') and request.user.is_authenticated:
#             response = HttpResponseRedirect('home')
#         else:
#             response = self.get_response(request)
#         return response