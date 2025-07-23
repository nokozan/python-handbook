from first_class_functions import greet
from closures import rate_limiter
from decorator_py import decorator_logger
from hof_wrappers import retry


if __name__ == "__main__":
    greet.Run_first_class_functions()
    rate_limiter.run_closure_limiter()
    decorator_logger.run_decorator_logger()
    retry.run_hof_retry()
