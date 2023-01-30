from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now


def storage_information_view(request):

    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit_data in visits:
        duration = visit_data.get_duration(now())
        non_closed_visits.append(
            {
                'who_entered': visit_data.passcard,
                'entered_at': localtime(visit_data.entered_at),
                'duration': visit_data.format_duration(duration),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
