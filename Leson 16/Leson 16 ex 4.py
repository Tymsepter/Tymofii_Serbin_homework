class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'a') as file:
            file.write(msg + '\n')
        super().__init__(msg)


try:
    raise CustomException("Something went wrong")
except CustomException as e:
    print("Exception occurred: ", e.msg)
