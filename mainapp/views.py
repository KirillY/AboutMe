from django.shortcuts import render, Http404
from datetime import datetime, date
from mainapp.models import Work, Education, Organization
from django.core.exceptions import ObjectDoesNotExist


# def calculate_age(born):
# today = date.today()
# return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# Create your views here.

def main(request):
    firstname = 'Kirill'
    lastname = 'Lapshin'
    born = date(year=1984, month=3, day=28)
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    place = 'Moscow region'
    ul = {
        'age': age,
        'born': born,
        'place': place
    }
    filler = 'Have no info about the person'
    return render(request, 'index.html', {'ul': ul, 'filler': filler, 'firstname': firstname, 'lastname': lastname})


def work(request):
    work_places = Work.objects.all()
    # ul = ['Hospital', 'Insurance company', 'Upwork']
    filler = 'Begins a career'
    return render(request, 'work.html', {'work_places': work_places, 'filler': filler})


def edu(request):
    learn_places = Education.objects.all()
    filler = ['Have no info about education']
    return render(request, 'edu.html', {'learn_places': learn_places, 'filler': filler})


def org(request, r_id):
    try:
        organization = Organization.objects.get(id=r_id)
    except ObjectDoesNotExist:
        raise Http404
    organization=get_object_or_404(Organization, id=r_id)
    return render(request, 'org.html', {'organization': organization})
