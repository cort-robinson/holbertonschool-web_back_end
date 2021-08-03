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
from datetime import datetime

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
        database=db_name,
        auth_plugin='mysql_native_password')


def main():
    """
    Implement a main function that takes no arguments and returns nothing.

    The function will obtain a database connection using get_db and retrieve
    all rows in the users table and display each row under a filtered format
    like this:
        [HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***;
        email=***; phone=***; ssn=***; password=***;
        ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b;
        last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible;
        MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);

    Filtered fields:
        * name
        * email
        * phone
        * ssn
        * password

    Only your main function should run when the module is executed.
    """
    db = get_db()
    formatter = RedactingFormatter(PII_FIELDS)
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM users;")
    for row in cursor:
        log = ''
        for k, v in row.items():
            if not isinstance(v, datetime):
                log += k + '=' + v + '; '
        print(formatter.format(logging.LogRecord(
            'user_data', logging.INFO, None, None, log, None, None)))


if __name__ == "__main__":
    main()
