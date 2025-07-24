from functools import partial


def format_log(level: str, message: str) -> str:
    return f"[{level.upper()}] {message}"


def run_partial_function():
    print("\n -- Partial Function : Log Formatter ==")

    info_log = partial(format_log, "INFO")
    warn_log = partial(format_log, "WARN")
    error_log = partial(format_log, "ERROR")

    print(info_log("Service started"))
    print(warn_log("CPU usage high"))
    print(error_log("Crash detected"))
