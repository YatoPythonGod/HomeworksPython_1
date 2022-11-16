import logging


def logger_calc(func):
    def wrapper(*args):
        logging.basicConfig(level=logging.DEBUG, filename="calc_log.log", format="%(asctime)s %(message)s",
                            datefmt='%d-%b-%y %H:%M:%S')
        logging.info(f'User input: {", ".join(map(str, args))}')

        try:
            result = func(*args)
            logging.info(f'Result: {result}')
            return result
        except ZeroDivisionError as error:
            logging.error(f'Error: {error}')
            return error
        except Exception as all_error:
            logging.error(f'Error: {all_error}')
            return all_error
    return wrapper


def logger_main_choice(func):
    def wrapper(*args):
        logging.basicConfig(level=logging.DEBUG, filename="calc_log.log", format="%(asctime)s %(message)s",
                            datefmt='%d-%b-%y %H:%M:%S')
        result = func(*args)
        logging.info(f'User choice: {result}')
        return result
    return wrapper