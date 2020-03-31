from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from drinkslist.google_search import run_google_search
import json

def index(request):
    context_dict = {}
    # if request.method == "POST":
    #     print(request.POST)
    #     # result = search(request)

    #     context_dict['result_list'] = request.POST
    #     # return HttpResponse(context_dict)
    # # else:
    # #     pass

    return render(request, 'drinkslist/index.html',context_dict)


def about(request):
    return HttpResponse("Drinks list about page.")


def contactus(request):
    return HttpResponse("Drinks list contact us page")


# AJAX Applied - search helper function : return the searching results of google & Site
def search(request):
    result_list = []
    query = ""
    if request.method == 'POST':
        # search engine selection
        selection = request.POST['search-selection']
        print(selection)
        # user query string
        query = request.POST['query'].strip()
        if query:
            if selection == "static":
                # default site static searching
                pass
            else:
                result_list = run_google_search(query)

    # print(result_list)

    return HttpResponse(json.dumps(result_list))