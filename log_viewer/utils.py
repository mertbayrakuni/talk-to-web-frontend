import io
import os
import re

from os import listdir
from os.path import isfile, join

from django.conf import settings

from core.settings import BASE_DIR


class LogManager:
    name = ""
    logs = []
    log_names = []
    columns = []
    log_files = []
    path = None

    def __init__(self):
        """
        Get all log file names as contained in log setting with the formatter for each.
        """
        self.formatters = '%(asctime)s | %(name)s | %(levelname)s | %(pathname)s | %(funcName)s | %(lineno)d | %(message)s'
        self.logs = []
        self.path = os.path.join(BASE_DIR, "logs")
        for root, dirs, files in os.walk(self.path, topdown=False):
            for file_name in files:
                if file_name.endswith(".log") and not file_name.startswith("_"):
                    self.log_names.append(file_name)
                    self.log_files.append(file_name)

    def get_logs(self):
        return self.log_names

    def load_details(self, name):
        """
        We have a log to deal with now. Get possible columns for this log file (using format setting) and load all
        old log files for the selected log file
        :param name:
        :return:
        """
        self.name = name
        self.columns = ["Date", "Name", "Level", "Path", "Func", "LineNo", "Msg"]
        _format = '%(asctime)s | %(name)s | %(levelname)s | %(pathname)s | %(funcName)s | %(lineno)d | %(message)s'
        for log in self.logs:
            filename = log.get('name')
            expected_default_name = '{}{}'.format(name, getattr(settings, 'LOG_FILE_EXTENSION', '.log'))
            if filename.endswith(expected_default_name):
                self.log_files = sorted([file for file in listdir(self.path) if
                                         isfile(join(self.path, file)) and file.__contains__(expected_default_name)])
                break

    def get_columns(self):
        return self.columns

    def get_log_files(self):
        return self.log_files

    def get_log_content(self, file):
        file_path = join(self.path, file)
        rows = []
        with io.open(file_path, encoding="utf-8") as log_file:
            lines = log_file.readlines()
            for line in lines:
                rows.append(line.split("|"))
        return rows
