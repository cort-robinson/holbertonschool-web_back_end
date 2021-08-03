#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated:

    * Arguments:
        * fields: a list of strings representing all fields to obfuscate
        * redaction: a string representing by what the field will be obfuscated
        * message: a string representing the log line
        * separator: a string representing by which character is separating
          all fields in the log line (message)
    * The function should use a regex to replace occurrences of certain field
      values.
    * filter_datum should be less than 5 lines long and use re.sub to perform
      the substitution with a single regex.
"""
import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum. Values for
        fields in fields should be filtered.

        DO NOT extrapolate FORMAT manually. The format method should be less
        than 5 lines long.
        """
        return filter_datum(
            self.fields, self.REDACTION, super().format(record),
            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Returns the log message obfuscated.

    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating
            all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(
            field + "=" + ".+?" + separator,
            field + "=" + redaction + separator,
            message)
    return message


def get_logger() -> logging.Logger:
    """
    Implement a get_logger function that takes no arguments and returns a
    logging.Logger object.

    The logger should be named "user_data" and only log up to logging.INFO
    level. It should not propagate messages to other loggers. It should have a
    StreamHandler with RedactingFormatter as formatter.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    In this task, you will connect to a secure holberton database to read a
    users table. The database is protected by a username and password that are
    set as environment variables on the server named PERSONAL_DATA_DB_USERNAME
    (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as
    an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”)

    The database name is stored in PERSONAL_DATA_DB_NAME.

    Implement a get_db function that returns a connector to the database
    (mysql.connector.connection.MySQLConnection object).

        * Use the os module to obtain credentials from the
          environment
        * Use the module mysql-connector-python to connect to the MySQL
          database (pip3 install mysql-connector-python)
    """
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME')
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD')
    host = os.environ.get('PERSONAL_DATA_DB_HOST')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name)
