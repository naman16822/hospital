from authentication.utils import send_email
from django.conf import settings

def CaseAssigned(user, casemanager, caseid):
    data = {
        'user': user.username,
        'case_manager': casemanager.username,
        'case_id': caseid,
    }
    
    send_email(
        template_name='case_assigned.txt',
        data=data,
        subject="Case Assigned",
        to=[user.email]
    )
    
    send_email(
        template_name='case_email.txt',
        data=data,
        subject="Case Assigned to your desk ",
        to=[casemanager.email]
    )