import time

from functools import wraps

from libs.common.Logger import logger

def exec_log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        if args and kwargs:
            logger.debug('INFO: Started executing {}({},{}) '.format(func.__qualname__, args, kwargs))
        elif args:
            logger.debug('INFO: Started executing {}({})'.format(func.__qualname__, args))
        elif kwargs:
            logger.debug('INFO: Started executing {}({})'.format(func.__qualname__, kwargs))
        else:
            logger.debug('INFO: Started executing {}()'.format(func.__qualname__))
        retval = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.debug("Info: Completed executing {} in {} seconds ".format(func.__qualname__, end_time))
        return retval
    return inner




