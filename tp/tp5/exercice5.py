class INotificationService(ABC):
    @abstractmethod
    def send(self, msg): pass

class EmailService(INotificationService):
    def send(self, msg): print(f"Email: {msg}")

class SMSService(INotificationService):
    def send(self, msg): print(f"SMS: {msg}")

class UserNotification:
    def __init__(self, service: INotificationService):
        self.service = service

    def notify(self, user, message):
        self.service.send(message)

email_notifier = UserNotification(EmailService())
sms_notifier = UserNotification(SMSService())