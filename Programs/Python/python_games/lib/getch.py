class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        basic_key = msvcrt.getch()
        if basic_key == b"\xe0":
            sub = msvcrt.getch()
            if sub == b'H':
                return 'UP_KEY'
            elif sub == b'M':
                return 'RIGHT_KEY'
            elif sub == b'P':
                return 'DOWN_KEY'
            elif sub == b'K':
                return 'LEFT_KEY'
            else:
                return sub
        else:
            return msvcrt.getch()

# Reference: Yoo, D. (2002). getch()-like unbuffered character reading from stdin on both 
#   windows and unix (Python recipe) [Source code].
#   Retreived from http://code.activestate.com/recipes/134892/
