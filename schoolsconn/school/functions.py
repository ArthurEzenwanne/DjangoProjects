

def slugify(s):
    """
    Simplifies ugly strings into something URL-friendly.
    """
    s = s.lower()
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')
    s = re.sub('\W', '', s)
    s = s.replace('_', ' ')
    s = re.sub('\s+', ' ', s)
    s = s.strip()
    s = s.replace(' ', '-')
    return s


def send_sms_message():
    '''Function to send sms message to School owner'''
    learner_name = form.learner_name
    learner_phone = form.learner_phone
    school_name = form.school_name
    school_phone = form.school_phone
    sms_message = 'Hi {school_name}, a parent {learner_name}, has indicated interest in your school on schoolsconn.com. Kindly connect with parent on {learner_phone}. Questions? SMS/WhatsApp +234 909 058 7701'
    sender_name = 'SchoolsConn'
    url = 'http://www.80kobosms.com/tools/geturl/Sms.php'
    params = {
        'username': '1994Chang',
        'password': 'enquire@schoolsconn.com',
        'sender': sender_name,
        'message': sms_message,
        'flash': 1,
        'recipients': school_phone,
        'forcednd': 1
    }
    r = requests.get(url=url, params=params)
