

class Googler:

    def __init__(self, value):
        self.response = GoogleSearch().search(value)

        for x in self.response:
            print(x)
