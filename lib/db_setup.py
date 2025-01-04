# import sql_commands as sql
import logging
import psycopg2
from lib.sql_commands import SQLCommands


class DB_setup:

    def __init__(self, context):
        self.context = context

    def setup_database(self, context):
        login = '(example)'
        logging.info('\nAdding user')
        self.setup_user_profile(context, login)
        logging.info('Done')
        logging.info('\nAdding user')

    def sql_commands_setup(self, context, sql_commands):
        for sql_command in sql_commands:
            try:
                sql_begin = 'BEGIN;'
                sql_commit = 'COMMIT;'
                sql_check_user = True
                if sql_check_user:
                    context.db.cursor.execute(sql_command[0])
                    results = context.db.cursor.fetchall()
                    if not results:
                        context.db.cursor.execute(sql_begin)
                        context.db.cursor.execute(sql_command[1])
                        context.db.cursor.execute(sql_commit)

            except psycopg2.errors.UniqueViolation as e:
                sql_rollback = 'ROLLBACK;'
                context.db.cursor.execute(sql_rollback)
                logging.error(f"Transaction rolled back due to error: {e}")

    def setup_user_profile(self, context, login):
        setup_user_profile = [SQLCommands.sql_example(f"{login}")]

        self.sql_commands_setup(sql_commands=setup_user_profile, context=context)
