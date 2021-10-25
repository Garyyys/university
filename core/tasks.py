from datetime import datetime

from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Student, Lecture
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def heart_beat():
    logger = get_task_logger(__name__)

    qs = Student.objects.filter(subscription=True)

    logger.debug('%d Students in queue for sending mails', qs.count())
    for obj in qs:
        lecture_qs = Lecture.objects.filter(group__students__pk=obj.pk).filter(start_time__date=datetime.now().date())
        lectures = [f"Название лекции: {lecture.lection_name}\n Преподаватель: {lecture.teacher}\n Вермя: {lecture.start_time}" for lecture in lecture_qs]
        message = '\n'.join(lectures)
        subject = f'Ваши лекции на {datetime.now().date()}'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [obj.email]
        )
