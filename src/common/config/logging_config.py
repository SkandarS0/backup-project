import logging

logging_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_logger = logging.getLogger("console_logger")
console_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging_formatter)
console_logger.addHandler(console_handler)

file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("backup.log", mode="a")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging_formatter)
file_logger.addHandler(file_handler)

console_file_logger = logging.getLogger("console_file_logger")
console_file_logger.setLevel(logging.DEBUG)
console_file_logger.addHandler(console_handler)
console_file_logger.addHandler(file_handler)
