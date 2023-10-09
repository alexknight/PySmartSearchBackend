# import logging
# from logging.handlers import TimedRotatingFileHandler
# import os
# from os.path import dirname
# import sys
# import datetime
#
#
# class Singleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
# class CustomFormatter(logging.Formatter):
#     def format(self, record):
#         record.asctime = datetime.datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S,%f')
#         return super(CustomFormatter, self).format(record)
#
# class ServiceLog(metaclass=Singleton):
#     def __init__(self, log_directory=os.path.join(dirname(dirname(__file__)), "log"), log_name='service'):
#         self.logger = logging.getLogger(log_name)
#         self.logger.setLevel(logging.DEBUG)
#
#         self.log_directory = log_directory
#         if not os.path.exists(self.log_directory):
#             os.makedirs(self.log_directory)
#
#         self.log_file_name = f'{log_name}_{datetime.date.today()}.log'
#         self.log_file_path = os.path.join(self.log_directory, self.log_file_name)
#
#         self.console_handler = logging.StreamHandler(sys.stdout)
#         self.console_handler.setLevel(logging.DEBUG)
#
#         self.file_handler = TimedRotatingFileHandler(self.log_file_path, when="midnight", interval=1, backupCount=30)
#         self.file_handler.setLevel(logging.DEBUG)
#
#         # 创建日志格式
#         log_format = CustomFormatter('{asctime}-{funcName}:{lineno} {message}', datefmt='%Y-%m-%d %H:%M:%S,%f', style='{')
#         self.console_handler.setFormatter(log_format)
#         self.file_handler.setFormatter(log_format)
#
#         self.logger.addHandler(self.console_handler)
#         self.logger.addHandler(self.file_handler)
#
#     def get_logger(self):
#         return self.logger
#
# logger = ServiceLog().get_logger()
#
