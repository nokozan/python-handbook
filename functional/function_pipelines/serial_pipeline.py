from typing import Callable, List


def strip_spaces(text: str) -> str:
    return text.strip()


def to_lowercase(text: str) -> str:
    return text.lower()


def add_prefix(text: str) -> str:
    return f"cleaned: {text}"


def make_pipeline(stages: List[Callable[[str], str]]) -> Callable[[str], str]:
    def runner(input_text: str) -> str:
        for stage in stages:
            input_text = stage(input_text)
        return input_text

    return runner


def run_serial_pipeline():
    print("\n -- Function pipeline : serial Execution")
    pipeline = make_pipeline(
        [
            strip_spaces,
            to_lowercase,
            add_prefix,
        ]
    )

    raw = " Hello !!! "
    result = pipeline(raw)
    print(f"Input {repr(raw)}")
    print(f"Output: {result}")
