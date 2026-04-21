# 📌 Strategy Design Pattern

## 🧠 Overview

The **Strategy Pattern** is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.

Instead of using large `if/elif` (or `switch`) statements, you delegate behavior to separate classes (strategies), making your code more flexible and maintainable.

---

## 🎯 When to Use Strategy Pattern

Use the Strategy Pattern when:

* You have multiple ways to perform a task (e.g., payment methods, notification types).
* You want to **avoid conditional logic** (`if/else`).
* You need to **add new behaviors without modifying existing code**.
* You want to follow the **Open/Closed Principle**.

---

## 🏗️ Structure

The Strategy Pattern typically consists of:

1. **Strategy Interface**
   Defines a common interface for all strategies.

2. **Concrete Strategies**
   Implement different variations of the behavior.

3. **Context (Client)**
   Uses a strategy and delegates the work to it.

---

## 📊 Simple Diagram

```
        +----------------------+
        |   Strategy (Interface) |
        +----------------------+
                  ▲
        ------------------------
        |          |           |
+--------------+ +--------------+ +--------------+
| EmailStrategy| | SMSStrategy  | | SlackStrategy|
+--------------+ +--------------+ +--------------+

                ▲
        +----------------------+
        |  NotificationService |
        +----------------------+
```

---

## 💡 Advantages

* ✅ Eliminates complex conditional logic
* ✅ Easy to extend (add new strategies)
* ✅ Follows SOLID principles
* ✅ Promotes clean and reusable code

---

## ⚠️ Disadvantages

* ❌ Increases number of classes
* ❌ Requires understanding of abstraction

---

# 🚀 Coding Exercise

## 📌 Problem Statement

You are developing a **notification service** that needs to support multiple types of notifications for users.

The system should be able to send notifications via:

* SMS
* Email
* Messenger
* Slack

---

## 🎯 Requirement

Implement a function:

```
sendNotification(user, message)
```

---

## ⚠️ Constraints

* Each notification type has its own sending logic.
* You should be able to **add new notification types without modifying existing code**.
* Avoid using `if/elif` statements.
* Follow clean code and object-oriented design principles.

---

# ✅ Solution (Strategy Pattern)

## 1️⃣ Strategy Interface

```python
from abc import ABC, abstractmethod

class NotificationStrategy(ABC):

    @abstractmethod
    def send(self, user, message: str):
        pass
```

---

## 2️⃣ Concrete Strategies

```python
class EmailNotification(NotificationStrategy):

    def send(self, user, message: str):
        print(f"Sending EMAIL to {user.email}: {message}")


class SMSNotification(NotificationStrategy):

    def send(self, user, message: str):
        print(f"Sending SMS to {user.phone}: {message}")


class SlackNotification(NotificationStrategy):

    def send(self, user, message: str):
        print(f"Sending Slack message to {user.slack_id}: {message}")


class MessengerNotification(NotificationStrategy):

    def send(self, user, message: str):
        print(f"Sending Messenger message to {user.messenger_id}: {message}")
```

---

## 3️⃣ Context (Notification Service)

```python
class NotificationService:

    def __init__(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def send_notification(self, user, message: str):
        self._strategy.send(user, message)
```

---

## 4️⃣ User Model

```python
class User:

    def __init__(self, name, email=None, phone=None, slack_id=None, messenger_id=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.slack_id = slack_id
        self.messenger_id = messenger_id
```

---

## 5️⃣ Usage Example

```python
def main():
    user = User(
        name="Mahmoud",
        email="mahmoud@example.com",
        phone="01012345678",
        slack_id="mahmoud.slack",
        messenger_id="mahmoud.messenger"
    )

    service = NotificationService(EmailNotification())
    service.send_notification(user, "Welcome via Email!")

    service.set_strategy(SMSNotification())
    service.send_notification(user, "Welcome via SMS!")

    service.set_strategy(SlackNotification())
    service.send_notification(user, "Welcome via Slack!")

    service.set_strategy(MessengerNotification())
    service.send_notification(user, "Welcome via Messenger!")


if __name__ == "__main__":
    main()
```

---

# 🔥 Key Takeaways

* Strategy Pattern helps you **replace conditional logic with polymorphism**.
* Each behavior is isolated in its own class.
* You can **add new features safely without breaking existing code**.
* This pattern is commonly used in:

  * Payment systems 💳
  * Notification systems 📩
  * Sorting/filtering logic 🔍

---

# 💯 Bonus Tip (Interview)

If asked in an interview:

> “Why use Strategy Pattern?”

You can say:

* It improves **maintainability**
* It follows **Open/Closed Principle**
* It makes the system **extensible and testable**

---

📌 *This example is a practical demonstration of applying Strategy Pattern in real-world scenarios.*
