'''
Build a logging system using the Factory Design Pattern.
Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger,
ConsoleLogger, DatabaseLogger). Implement methods in each logger to write logs to
their respective destinations. Show how the Factory Design Pattern helps to decouple
the logging system from the application and allows for flexible log handling.
'''

# create an object from the different places where we use them 
# factory class does the creation for the object rather than in the main function 

from abc import ABC, abstractmethod



class Logger(ABC): 
    @abstractmethod 
    def log(): 
        """Generates the Log"""

class FileLogger(Logger): 

    def log(self, message):
        """Writes a Log to the log.txt 

        Args:
            message (str): message to write the log 
        """
        with open('log.txt', "a") as f: 
            f.write(message + "\n") 

class ConsoleLogger(Logger): 
    def log(self, message): 
        print(message)

class DatabaseLogger(Logger): 
    def log(self, message): 
        print(f"{message} has been Logged to the Database")



class FactoryLogger: 
    def get_logger(self, logger_type): 
        if logger_type == "file": 
            return FileLogger()
        
        elif logger_type =="database": 
            return DatabaseLogger()
        
        elif logger_type == "console": 
            return ConsoleLogger()



faclog = FactoryLogger()
flogger = faclog.get_logger("file")

for i in range(5): 
    flogger.log("Writing log files ")