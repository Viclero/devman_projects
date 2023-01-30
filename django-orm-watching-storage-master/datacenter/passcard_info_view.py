from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit_data in visits:
        duration = visit_data.get_duration(visit_data.leaved_at)
        this_passcard_visits.append(
            {
                'entered_at': visit_data.entered_at,
                'duration': visit_data.format_duration(duration),
                'is_strange': visit_data.is_visit_long()
            },
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
