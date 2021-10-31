from django.http.response import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    entries = util.list_entries()
    title = title.upper()
    for entry in entries:
        if title == entry.upper():
            return render(request,"encyclopedia/entry.html",{"Title":title.upper(), "content":util.get_entry(title)})
    else:
        return render(request,"encyclopedia/noentryerror.html")

