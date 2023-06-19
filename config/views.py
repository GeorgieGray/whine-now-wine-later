from django.shortcuts import render

def custom_page_not_found_view(request, exception):
    return render(request, "oops.html", { "status_code": 404 })

def custom_error_view(request, exception=None):
    return render(request, "oops.html", { "status_code": 500 })

def custom_permission_denied_view(request, exception=None):
    return render(request, "oops.html", { "status_code": 403 })

def custom_bad_request_view(request, exception=None):
    return render(request, "oops.html", { "status_code": 400 })