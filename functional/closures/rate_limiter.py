from typing import Callable


def make_limiter(max_calls: int) -> Callable[[str], str]:
    quota = max_calls

    def limited_action(user: str) -> str:
        nonlocal quota
        if quota > 0:
            quota -= 1
            return f"[OK] Action allowed for {user} ({quota} left)"
        else:
            return f"[DENY] Rate limit exceeded for {user}"

    return limited_action


def run_closure_limiter():
    print("\n == Closure: Rate Limiter ==")
    limiter = make_limiter(2)
    print(limiter("alice"))
    print(limiter("bob"))
    print(limiter("charlie"))
