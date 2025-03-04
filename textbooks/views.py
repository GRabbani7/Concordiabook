from django.shortcuts import render
from .models import Textbook

def textbook_list(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)

    no_results = not textbooks.exists()

    context = {
        'textbooks': textbooks,
        'course_code': course_code,
        'no_results': no_results,
    }

    return render(request, 'textbooks/textbook_list.html', context)