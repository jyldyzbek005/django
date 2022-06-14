#
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("""'<h1>hello world</h1>
#         <h2>hello</h2>
#         <h3>hello</h3>
#         <h5>ты красивый парень</h5>""")


from django .shortcuts import render


def index(request):
    return render (request, 'index.html')