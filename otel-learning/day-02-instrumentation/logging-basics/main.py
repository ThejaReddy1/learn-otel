import time
import logging
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry._logs import set_logger_provider, get_logger, LogRecord
from opentelemetry.sdk._logs.export import ConsoleLogExporter, ConsoleLogRecordExporter, BatchLogRecordProcessor
from opentelemetry._logs import SeverityNumber

logger_provider = LoggerProvider()
# exporter = ConsoleLogExporter()  # Deprecated
# exporter = ConsoleLogRecordExporter()
# exporter = ConsoleLogExporter()
# NOTE: The original code had commented out exporters. 
# Using ConsoleLogExporter for demonstration if needed, but keeping original logic.
exporter = ConsoleLogExporter() 

processor = BatchLogRecordProcessor(exporter=exporter, export_timeout_millis=5000)  # buffers the records and call the exporter with bath on a schedule or when the queue limit is reached.

logger_provider.add_log_record_processor(processor)     # Assigning the record processor to the log provider

set_logger_provider(logger_provider=logger_provider)                   # making the logger provider global

logger = get_logger("flight-booking","0.1.2")           # creating a logger and we will use this logger objects to create the log

handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)    # Using python Standard libray for logs generation and it's going to pass to opentelemetry 
logging.basicConfig(handlers=[handler], level=logging.NOTSET)

def book_flight():
    # print("strating the booking flight process")
    # logger.emit(LogRecord(body="Strating the booking flight process", timestamp=time.time_ns(), severity_text="INFO", severity_number=SeverityNumber.INFO))    # this emit function expects log record object
    logging.info("Strating the booking flight process")
    search_flights()
    reserve_flight()


def search_flights():
    logging.info("Searching for flights")
    pass
    # print("searching for flights.....")

def reserve_flight():
    logging.warn("Reserving flight")
    pass
    # print("Reserving flight")

if __name__ == "__main__":
    book_flight()
