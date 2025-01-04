class SQLCommands:
    parameter_test_dict = {''}

    @staticmethod
    def sql_example(login_example):
        ext = login_example.split('.')[1]
        example = SQLCommands.parameter_test_dict[ext]
        return (
            f"""## SQL command to check if already exist the data to insert into the table""",
            f"""## SQL command to insert some data""")


