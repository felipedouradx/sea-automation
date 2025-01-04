import logging
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Automatically reset the color codes after every print


class Formatter(logging.Formatter):

    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)
        self.keywords = {
            'Scenario Name': Fore.YELLOW + Style.BRIGHT,
            'Duration': Fore.WHITE + Style.BRIGHT,
            'Step Name': Fore.CYAN + Style.BRIGHT,
            'Status ': Fore.WHITE + Style.BRIGHT,
            'Status.passed': Fore.GREEN,
            'Status.failed': Fore.RED + Style.BRIGHT
        }

    def format(self, record):
        message = super().format(record)
        # Apply color to specific keywords found in the message
        for keyword, color in self.keywords.items():
            message = message.replace(keyword, f'{color}{keyword}{Style.RESET_ALL}')
        return message


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.handlers = [logger.handlers[0]]  # Fix for logs showing multiple times
