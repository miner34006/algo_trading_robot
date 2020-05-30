import logging

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)


def get_logger(module_name):
    """ Function to get logger based on name

    :param module_name: module name
    :type module_name: str
    :return: logger for logging
    :rtype: logging.Logger
    """
    return logging.getLogger(module_name)