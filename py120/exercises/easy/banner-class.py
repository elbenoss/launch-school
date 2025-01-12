# Complete this class so that the test cases shown below work as intended. 
# You are free to add any methods or instance variables you need. 
# However, methods prefixed with an underscore are intended for internal use and should not be called externally.

class Banner:
    def __init__(self, message):
        self.message = message
        self.width = len(self.message) + 2

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return "|" + " " * self.width + "|"

    def _horizontal_rule(self):
        return "+" + "-" * self.width + "+"

    def _message_line(self):
        return f"| {self.message} |"



    # Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+
