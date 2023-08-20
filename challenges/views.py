from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "January? i'm eat no meat for the entire month!",
    "february": "February? i'm walk for at least 20 minutes every day!",
    "march": "March? i'm learn Django for at least 20 minutes every day!",
    "april": "April? i'm eat no meat for the entire month!",
    "may": "May? i'm walk for at least 20 minutes every day!",
    "june": "June? i'm learn Django for at least 20 minutes every day!",
    "july": "July? i'm eat no meat for the entire month!",
    "august": "August? i'm walk for at least 20 minutes every day!",
    "september": "September? i'm learn Django for at least 20 minutes every day!",
    "october": "October? i'm eat no meat for the entire month!",
    "november": "November? i'm walk for at least 20 minutes every day!",
    "december": "December? i'm learn Django for at least 20 minutes every day!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported =)</h1>")
    return HttpResponse(challenge_text)

