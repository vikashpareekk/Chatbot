from django.shortcuts import render
from django.http import JsonResponse
from .models import Subject, Teacher, Availability

def chatbot_page(request):
    return render(request, 'chatbot.html')

def chatbot_api(request):
    step = request.GET.get('step', 'start')
    response = {}

    if step == 'start':
        response = {
            "message": "Hi! How can I help you today?",
            "options": [
                {"label": "Choose Subject", "next": "choose_subject"},
                {"label": "Doubt", "next": "doubt_subject"}
            ]
        }

    elif step == 'choose_subject':
        subjects = Subject.objects.all()
        response = {
            "message": "Here are the available subjects:",
            "options": [
                {"label": str(s.name), "link": s.website_link or ""}
                for s in subjects
            ]
        }

    elif step == 'doubt_subject':
        subjects = Subject.objects.all()
        response = {
            "message": "In which subject do you have a doubt?",
            "options": [
                {"label": str(s.name), "next": f"choose_teacher_{s.id}"}
                for s in subjects
            ]
        }

    elif step.startswith('choose_teacher_'):
        subject_id = step.split('_')[-1]
        teachers = Teacher.objects.filter(subject_id=subject_id)
        response = {
            "message": "Select a teacher:",
            "options": [
                {"label": str(t.name), "next": f"teacher_time_{t.id}"}
                for t in teachers
            ]
        }

    elif step.startswith('teacher_time_'):
        teacher_id = step.split('_')[-1]
        times = Availability.objects.filter(teacher_id=teacher_id)
        response = {
            "message": "Available times for this teacher:",
            "options": [
                {"label": str(a.time_slot)}
                for a in times
            ]
        }

    return JsonResponse(response)
