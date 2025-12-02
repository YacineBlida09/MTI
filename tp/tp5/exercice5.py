from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import uuid

# ============ STEP 1: ABSTRACT INTERFACES ============

class NotificationService(ABC):
    """Abstract interface for all notification services"""
    
    @abstractmethod
    def send(self, recipient: str, message: str, **kwargs) -> Dict[str, Any]:
        """Send notification and return delivery status"""
        pass
    
    @abstractmethod
    def get_service_name(self) -> str:
        """Get name of the notification service"""
        pass
    
    @abstractmethod
    def supports_priority(self) -> bool:
        """Check if service supports priority levels"""
        pass
    
    @abstractmethod
    def validate_recipient(self, recipient: str) -> bool:
        """Validate recipient address/identifier"""
        pass

# ============ STEP 2: CONCRETE IMPLEMENTATIONS ============

class EmailService(NotificationService):
    def __init__(self, smtp_server: str = "smtp.example.com", port: int = 587):
        self.smtp_server = smtp_server
        self.port = port
        self.connection_active = False
    
    def connect(self):
        """Simulate connection to SMTP server"""
        self.connection_active = True
        print(f"[Email] Connected to {self.smtp_server}:{self.port}")
    
    def disconnect(self):
        self.connection_active = False
        print("[Email] Disconnected from SMTP server")
    
    def send(self, recipient: str, message: str, **kwargs) -> Dict[str, Any]:
        if not self.connection_active:
            self.connect()
        
        subject = kwargs.get('subject', 'Notification')
        priority = kwargs.get('priority', 'normal')
        
        # Simulate email sending
        print(f"[Email] To: {recipient}")
        print(f"[Email] Subject: {subject}")
        print(f"[Email] Priority: {priority}")
        print(f"[Email] Body: {message[:50]}...")
        
        # Simulate delivery status
        return {
            "status": "delivered",
            "service": "email",
            "recipient": recipient,
            "message_id": f"email_{uuid.uuid4().hex[:8]}",
            "timestamp": datetime.now().isoformat(),
            "details": {
                "smtp_server": self.smtp_server,
                "priority": priority
            }
        }
    
    def get_service_name(self) -> str:
        return "Email Notification Service"
    
    def supports_priority(self) -> bool:
        return True
    
    def validate_recipient(self, recipient: str) -> bool:
        return "@" in recipient and "." in recipient

class SMSService(NotificationService):
    def __init__(self, api_key: str, sender_id: str = "NOTIFY"):
        self.api_key = api_key
        self.sender_id = sender_id
        self.sms_count = 0
    
    def send(self, recipient: str, message: str, **kwargs) -> Dict[str, Any]:
        # Validate phone number
        if not self.validate_recipient(recipient):
            raise ValueError(f"Invalid phone number: {recipient}")
        
        # Simulate SMS sending
        print(f"[SMS] From: {self.sender_id}")
        print(f"[SMS] To: {recipient}")
        print(f"[SMS] Message: {message[:160]}...")  # SMS length limit
        
        self.sms_count += 1
        
        return {
            "status": "sent",
            "service": "sms",
            "recipient": recipient,
            "message_id": f"sms_{self.sms_count:06d}",
            "timestamp": datetime.now().isoformat(),
            "details": {
                "characters": len(message),
                "sender_id": self.sender_id
            }
        }
    
    def get_service_name(self) -> str:
        return "SMS Gateway Service"
    
    def supports_priority(self) -> bool:
        return False
    
    def validate_recipient(self, recipient: str) -> bool:
        # Simple phone validation
        return recipient.startswith("+") and recipient[1:].isdigit() and len(recipient) >= 10

class PushNotificationService(NotificationService):
    def __init__(self, app_id: str):
        self.app_id = app_id
        self.device_tokens = {}
    
    def register_device(self, user_id: str, device_token: str):
        self.device_tokens[user_id] = device_token
        print(f"[Push] Registered device for user {user_id}")
    
    def send(self, recipient: str, message: str, **kwargs) -> Dict[str, Any]:
        # Check if device is registered
        if recipient not in self.device_tokens:
            return {
                "status": "failed",
                "error": "Device not registered",
                "service": "push",
                "recipient": recipient,
                "timestamp": datetime.now().isoformat()
            }
        
        # Get additional parameters
        title = kwargs.get('title', 'Notification')
        badge = kwargs.get('badge', 1)
        
        # Simulate push notification
        device_token = self.device_tokens[recipient]
        print(f"[Push] Title: {title}")
        print(f"[Push] To device: {device_token[:10]}...")
        print(f"[Push] Message: {message}")
        print(f"[Push] Badge: {badge}")
        
        return {
            "status": "delivered",
            "service": "push",
            "recipient": recipient,
            "device_token": device_token[:8] + "...",
            "timestamp": datetime.now().isoformat(),
            "details": {
                "title": title,
                "badge": badge,
                "app_id": self.app_id
            }
        }
    
    def get_service_name(self) -> str:
        return f"Push Service (App: {self.app_id})"
    
    def supports_priority(self) -> bool:
        return True
    
    def validate_recipient(self, recipient: str) -> bool:
        return recipient in self.device_tokens

class SlackService(NotificationService):
    def __init__(self, webhook_url: str, channel: str = "#general"):
        self.webhook_url = webhook_url
        self.channel = channel
    
    def send(self, recipient: str, message: str, **kwargs) -> Dict[str, Any]:
        # Simulate Slack webhook call
        username = kwargs.get('username', 'NotificationBot')
        icon_emoji = kwargs.get('icon_emoji', ':bell:')
        
        print(f"[Slack] Channel: {self.channel}")
        print(f"[Slack] To: @{recipient}")
        print(f"[Slack] From: {username} {icon_emoji}")
        print(f"[Slack] Message: {message}")
        
        return {
            "status": "posted",
            "service": "slack",
            "channel": self.channel,
            "recipient": recipient,
            "timestamp": datetime.now().isoformat(),
            "details": {
                "username": username,
                "icon_emoji": icon_emoji,
                "webhook": self.webhook_url[:20] + "..."
            }
        }
    
    def get_service_name(self) -> str:
        return "Slack Integration Service"
    
    def supports_priority(self) -> bool:
        return False
    
    def validate_recipient(self, recipient: str) -> bool:
        # Slack usernames typically don't contain spaces
        return len(recipient) > 0 and ' ' not in recipient

# ============ STEP 3: DATA MODELS ============

@dataclass
class User:
    """User data model"""
    id: str
    name: str
    email: str
    phone: Optional[str] = None
    slack_id: Optional[str] = None
    push_token: Optional[str] = None
    
    def get_preferred_contact(self) -> str:
        """Get user's preferred contact method"""
        if self.email:
            return self.email
        elif self.phone:
            return self.phone
        elif self.slack_id:
            return self.slack_id
        else:
            return self.id

@dataclass
class Notification:
    """Notification data model"""
    id: str
    user_id: str
    message: str
    priority: str = "normal"
    category: str = "general"
    created_at: datetime = datetime.now()
    
    def format_message(self, user_name: str) -> str:
        """Format message with personalization"""
        return f"Hello {user_name},\n\n{self.message}\n\nThank you!"

# ============ STEP 4: HIGH-LEVEL MODULE (DIP COMPLIANT) ============

class UserNotification:
    """High-level module that depends on abstractions"""
    
    def __init__(self, notification_services: List[NotificationService]):
        """
        Constructor injection of notification services
        Depends on abstract NotificationService, not concrete implementations
        """
        self.services = notification_services
        self.notification_history = []
    
    def notify_user(self, user: User, notification: Notification) -> List[Dict[str, Any]]:
        """
        Send notification to user through all available services
        Returns delivery status from each service
        """
        results = []
        
        # Format the message
        formatted_message = notification.format_message(user.name)
        
        # Try each service
        for service in self.services:
            # Determine recipient based on service type
            recipient = self._get_recipient_for_service(user, service)
            if not recipient:
                continue  # User doesn't have this contact method
            
            # Prepare service-specific parameters
            kwargs = self._prepare_service_kwargs(service, notification)
            
            try:
                # Send notification
                result = service.send(recipient, formatted_message, **kwargs)
                result['user_id'] = user.id
                result['notification_id'] = notification.id
                results.append(result)
                
                # Log to history
                self.notification_history.append({
                    'timestamp': datetime.now(),
                    'user': user.name,
                    'service': service.get_service_name(),
                    'status': result.get('status', 'unknown'),
                    'message': notification.message[:50] + "..."
                })
                
            except Exception as e:
                error_result = {
                    'status': 'failed',
                    'service': service.get_service_name(),
                    'error': str(e),
                    'user_id': user.id,
                    'timestamp': datetime.now().isoformat()
                }
                results.append(error_result)
        
        return results
    
    def _get_recipient_for_service(self, user: User, service: NotificationService) -> Optional[str]:
        """Get appropriate recipient identifier for each service type"""
        service_name = service.get_service_name().lower()
        
        if 'email' in service_name and user.email:
            return user.email
        elif 'sms' in service_name and user.phone:
            return user.phone
        elif 'slack' in service_name and user.slack_id:
            return user.slack_id
        elif 'push' in service_name and user.push_token:
            return user.push_token
        return None
    
    def _prepare_service_kwargs(self, service: NotificationService, notification: Notification) -> Dict[str, Any]:
        """Prepare service-specific parameters"""
        kwargs = {}
        
        if service.supports_priority():
            kwargs['priority'] = notification.priority
        
        # Service-specific parameters
        if isinstance(service, EmailService):
            kwargs['subject'] = f"Notification: {notification.category}"
        elif isinstance(service, PushNotificationService):
            kwargs['title'] = notification.category.capitalize()
            kwargs['badge'] = 1
        
        return kwargs
    
    def get_notification_history(self) -> List[Dict]:
        """Get history of all notifications sent"""
        return self.notification_history
    
    def get_service_statistics(self) -> Dict[str, Any]:
        """Get statistics about notification services"""
        stats = {
            'total_notifications': len(self.notification_history),
            'services_used': {},
            'success_rate': 0
        }
        
        successful = 0
        for entry in self.notification_history:
            service = entry['service']
            stats['services_used'][service] = stats['services_used'].get(service, 0) + 1
            
            if entry['status'] == 'delivered' or entry['status'] == 'sent' or entry['status'] == 'posted':
                successful += 1
        
        if self.notification_history:
            stats['success_rate'] = (successful / len(self.notification_history)) * 100
        
        return stats

# ============ STEP 5: FACTORY FOR CREATING SERVICES ============

class NotificationServiceFactory:
    """Factory for creating notification services (optional but useful)"""
    
    @staticmethod
    def create_email_service(smtp_server: str = None, port: int = None) -> EmailService:
        config = {
            'smtp_server': smtp_server or "smtp.gmail.com",
            'port': port or 587
        }
        return EmailService(**config)
    
    @staticmethod
    def create_sms_service(api_key: str = None) -> SMSService:
        api_key = api_key or "demo_api_key_12345"
        return SMSService(api_key=api_key, sender_id="APP")
    
    @staticmethod
    def create_push_service(app_id: str = None) -> PushNotificationService:
        app_id = app_id or "com.example.app"
        return PushNotificationService(app_id=app_id)
    
    @staticmethod
    def create_slack_service(webhook_url: str = None, channel: str = None) -> SlackService:
        webhook_url = webhook_url or "https://hooks.slack.com/services/..."
        channel = channel or "#notifications"
        return SlackService(webhook_url=webhook_url, channel=channel)
    
    @staticmethod
    def create_all_services() -> List[NotificationService]:
        """Create all available notification services"""
        return [
            NotificationServiceFactory.create_email_service(),
            NotificationServiceFactory.create_sms_service(),
            NotificationServiceFactory.create_push_service(),
            NotificationServiceFactory.create_slack_service()
        ]

# ============ STEP 6: USAGE EXAMPLE ============

def main():
    """Demonstration of DIP-compliant notification system"""
    
    print("=" * 60)
    print("DEPENDENCY INVERSION PRINCIPLE DEMONSTRATION")
    print("=" * 60)
    
    # 1. Create notification services using factory
    print("\n1. Creating notification services...")
    factory = NotificationServiceFactory()
    services = factory.create_all_services()
    
    # Register a device for push notifications
    push_service = services[2]  # PushNotificationService
    push_service.register_device("user123", "device_token_abc123xyz")
    
    # 2. Create UserNotification with injected services
    print("\n2. Creating UserNotification with injected services...")
    user_notification = UserNotification(services)
    
    # 3. Create a user with multiple contact methods
    print("\n3. Creating user with multiple contact methods...")
    user = User(
        id="user123",
        name="John Doe",
        email="john.doe@example.com",
        phone="+1234567890",
        slack_id="johndoe",
        push_token="device_token_abc123xyz"
    )
    
    # 4. Create a notification
    print("\n4. Creating notification...")
    notification = Notification(
        id=str(uuid.uuid4()),
        user_id=user.id,
        message="Your account has been successfully verified. You can now access all features.",
        priority="high",
        category="account"
    )
    
    # 5. Send notification
    print("\n5. Sending notification through all available channels...")
    print("-" * 40)
    results = user_notification.notify_user(user, notification)
    
    # 6. Display results
    print("\n6. Notification Results:")
    print("-" * 40)
    for i, result in enumerate(results, 1):
        print(f"\nChannel {i}: {result.get('service', 'Unknown')}")
        print(f"  Status: {result.get('status', 'unknown')}")
        print(f"  Recipient: {result.get('recipient', 'N/A')}")
        if 'error' in result:
            print(f"  Error: {result['error']}")
    
    # 7. Show statistics
    print("\n7. System Statistics:")
    print("-" * 40)
    stats = user_notification.get_service_statistics()
    print(f"Total notifications sent: {stats['total_notifications']}")
    print(f"Success rate: {stats['success_rate']:.1f}%")
    print("\nServices used:")
    for service, count in stats['services_used'].items():
        print(f"  - {service}: {count} times")
    
    # 8. Demonstrate adding a new service WITHOUT modifying UserNotification
    print("\n8. Demonstrating extensibility (adding Telegram service)...")
    print("-" * 40)
    
    # New service implementation
    class TelegramService(NotificationService):
        def __init__(self, bot_token: str):
            self.bot_token = bot_token
        
        def send(self, recipient: str, message: str, **kwargs) -> Dict[str, Any]:
            print(f"[Telegram] To chat: {recipient}")
            print(f"[Telegram] Message: {message[:100]}...")
            
            return {
                "status": "sent",
                "service": "telegram",
                "recipient": recipient,
                "message_id": f"tg_{uuid.uuid4().hex[:8]}",
                "timestamp": datetime.now().isoformat()
            }
        
        def get_service_name(self) -> str:
            return "Telegram Bot Service"
        
        def supports_priority(self) -> bool:
            return False
        
        def validate_recipient(self, recipient: str) -> bool:
            return recipient.isdigit()  # Telegram chat IDs are numbers
    
    # Add the new service dynamically
    telegram_service = TelegramService(bot_token="12345:ABC-DEF1234")
    
    # Update user with Telegram ID
    user_with_telegram = User(
        id="user456",
        name="Jane Smith",
        email="jane@example.com",
        phone="+9876543210",
        slack_id="janesmith"
    )
    # Note: We can't add telegram_id to existing User class without modifying it,
    # but in real scenario, we'd extend the User model
    
    # Create new notification system with Telegram
    all_services_with_telegram = services + [telegram_service]
    extended_notification = UserNotification(all_services_with_telegram)
    
    print("\n✓ Telegram service added WITHOUT modifying UserNotification class!")
    print("✓ DIP principle maintained: High-level module depends on abstraction")
    
    print("\n" + "=" * 60)
    print("DIP BENEFITS DEMONSTRATED:")
    print("=" * 60)
    print("1. UserNotification depends on NotificationService (abstraction)")
    print("2. Easy to add new notification channels")
    print("3. Easy to test (can inject mock services)")
    print("4. Low coupling between components")
    print("5. Flexibility to configure services at runtime")

# ============ STEP 7: TESTING WITH MOCKS ============

class MockNotificationService(NotificationService):
    """Mock service for testing"""
    def __init__(self):
        self.sent_messages = []
    
    def send(self, recipient: str, message: str, **kwargs) -> Dict[str, Any]:
        self.sent_messages.append({
            'recipient': recipient,
            'message': message,
            'kwargs': kwargs
        })
        return {
            'status': 'delivered',
            'service': 'mock',
            'recipient': recipient,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_service_name(self) -> str:
        return "Mock Notification Service"
    
    def supports_priority(self) -> bool:
        return True
    
    def validate_recipient(self, recipient: str) -> bool:
        return True

def test_user_notification():
    """Unit test demonstrating DIP benefits for testing"""
    print("\n" + "=" * 60)
    print("TESTING WITH MOCK SERVICES")
    print("=" * 60)
    
    # Create mock service
    mock_service = MockNotificationService()
    
    # Inject mock into UserNotification
    test_notification = UserNotification([mock_service])
    
    # Create test user and notification
    test_user = User(id="test123", name="Test User", email="test@example.com")
    test_notification_msg = Notification(
        id="test-notification",
        user_id=test_user.id,
        message="Test message",
        priority="normal"
    )
    
    # Send notification
    results = test_notification.notify_user(test_user, test_notification_msg)
    
    # Verify
    assert len(results) == 1
    assert results[0]['status'] == 'delivered'
    assert len(mock_service.sent_messages) == 1
    assert mock_service.sent_messages[0]['recipient'] == 'test@example.com'
    
    print("✓ Test passed! Mock service was successfully injected")
    print("✓ UserNotification is fully testable")
    print(f"✓ Mock recorded {len(mock_service.sent_messages)} message(s)")

# Run the demonstration
if __name__ == "__main__":
    main()
    test_user_notification()