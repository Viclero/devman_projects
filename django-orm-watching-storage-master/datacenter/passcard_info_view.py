from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visit = Visit.objects.filter(passcard=passcard)[0]

    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': Visit.format_duration( visit.leaved_at - visit.entered_at),
            'is_strange': visit.is_visit_long()
        },
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
