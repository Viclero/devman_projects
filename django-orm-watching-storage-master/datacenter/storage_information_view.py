from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request): 
    
    visits  = Visit.objects.filter(leaved_at=None)
    non_closed_visits=[]
    for v in visits: 
        duration = v.get_duration()
        non_closed_visits.append(
            {
                'who_entered': v.passcard,
                'entered_at': localtime(v.entered_at),
                'duration': Visit.format_duration(duration),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)
