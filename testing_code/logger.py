from __future__ import absolute_import
import logging


def setup_logger(logger_name, log_file, level=logging.INFO):
    my_log = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    my_log.setLevel(level)
    my_log.addHandler(fileHandler)
    my_log.addHandler(streamHandler)


def main():
    setup_logger('log1', r'.\log1.log', logging.WARNING)
    setup_logger('log2', r'.\log2.log')
    log1 = logging.getLogger('log1')
    log2 = logging.getLogger('log2')

    log1.info('Info for log 1!')
    log2.info('Info for log 2!')
    log1.error('Oh, no! Something went wrong!')


if '__main__' == __name__:
    main()
