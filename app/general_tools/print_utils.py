
# console codes
WARNING = '\033[95m'
OK_BLUE = '\033[94m'
NOTICE = '\033[93m'
FAIL = '\033[91m'
END_CODE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def print_with_header(header, message, color, indent=0):
    """
    Use one of the functions below for printing, not this one.
    """
    print()
    padding = ' ' * indent
    print(padding + color + BOLD + header + END_CODE + color + message + END_CODE)


def print_error(error_msg, indent=0):
    print_with_header('ERROR: ', error_msg, FAIL, indent)


def print_warning(warning_msg, indent=0):
    print_with_header('WARNING: ', warning_msg, WARNING, indent)


def print_notice(notice_msg, indent=0):
    print_with_header('NOTICE: ', notice_msg, NOTICE, indent)


def print_ok(ok_header, ok_message, indent=0):
    print_with_header(ok_header, ok_message, OK_BLUE, indent)


if __name__ == '__main__':
    pass
