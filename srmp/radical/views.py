from django.shortcuts import render, redirect
from .models import Maladie,Villes
import openai


# openai.api_key = ""

def home(request):
    maladieville ={
        'maladie': Maladie.objects.all(),
        'ville': Villes.objects.all(),
    }
    return render(request,"pages\home.html", maladieville)


def innerpage(request):
    return render(request,"pages\inner-page.html")

def service(request):
    return render(request,"pages\services.html")

def propos(request):
    return render(request,"pages/about.html")

def contact(request):
    return render(request,"pages/contact.html")



### Systeme de recommandation


def recommend_doctors(request):
    if request.method == 'POST':
        city = request.POST['ville']
        specialty = request.POST['symptoms']

        # Appel à OpenAI pour générer la recommandation des médecins
        openai.api_key = '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'
        prompt = f"Recommander des médecins à {city} spécialisés en {specialty},\
                    et donnez leurs adresse et telephone si c'est possible."
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.7,
            # n=5,
            stop=None,
            max_tokens=500,
        )

        choices_text = response['choices'][0]['text']
        doctors = choices_text[2:-2].split("\n")

        return render(request, 'pages/recommend_doctors.html', {'doctors': doctors})

    return render(request, 'pages/recommend_doctors.html')


def produit(request):
    return render(request,"pages/produit.html")



def doctor_specialties(request):
    return render(request,"pages/specialites.html")