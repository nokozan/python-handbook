from typing import Callable


def email_formatter(name: str) -> str:
    return f"Email sent to{name}"


def slack_formatter(name: str) -> str:
    return f"Slack message to {name}"


def notify(name: str, formatter: Callable[[str], str]) -> str:
    return formatter(name)


def Run_first_class_functions():
    users = ["Alice", "Bob", "Charlie"]

    print("== email notification")
    for name in users:
        msg = notify(name, email_formatter)
        print(msg)

    print("\n== slack notification")
    for name in users:
        msg = notify(name, slack_formatter)
        print(msg)
