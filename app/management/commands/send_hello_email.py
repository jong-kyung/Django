from django.template.loader import render_to_string
from django.core.management import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.conf import settings # 장고의 default settings와 프로젝트의 settings를 알아서 합쳐줌
from typing import List

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('receiver', nargs='+', type=str, help='이메일 수신자 주소')
    
    def handle(self, *args, **options):
        subject = render_to_string('app/hello_email_subject.txt')
        content = render_to_string('app/hello_email_content.txt', {
            'event_name' : '장고 연습 이벤트'
        })
        sender_email = settings.DEFAULT_FROM_EMAIL # 여기에서의 settings는 무조건 django.conf로 import
        receiver_email_list: List[str] = options['receiver']

        try:
            for email in receiver_email_list:
                validate_email(email)
        except ValidationError as e:
            raise CommandError(e.message)
        
        send_mail(
            subject,
            content,
            sender_email,
            receiver_email_list,
            fail_silently = False
        )