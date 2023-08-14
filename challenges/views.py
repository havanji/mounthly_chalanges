from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "January?, i'm eat no meat for the entire month!",
    "february": "February?, i'm walk for at least 20 minutes every day!",
    "march": "March?, i'm learn Django for at least 20 minutes every day!",
    "april": "April?, i'm eat no meat for the entire month!",
    "may": "May?, i'm walk for at least 20 minutes every day!",
    "june": "June?, i'm learn Django for at least 20 minutes every day!",
    "july": "July?, i'm eat no meat for the entire month!",
    "august": "August?, i'm walk for at least 20 minutes every day!",
    "september": "September?, i'm learn Django for at least 20 minutes every day!",
    "october": "October?, i'm eat no meat for the entire month!",
    "november": "November?, i'm walk for at least 20 minutes every day!",
    "december": "December?, i'm learn Django for at least 20 minutes every day!"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported =)")
    return HttpResponse(challenge_text)


