from datetime import datetime

def year_processor(request):
    return {
        'current_year': datetime.now().year
    }