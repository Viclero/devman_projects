from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request): 
    
    visits  = Visit.objects.filter(leaved_at=None)
    non_closed_visits=[]
    for visit_data in visits: 
        duration = visit_data.get_duration()
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
