class SmartLight:
    def __init__(self, location):
        self.location = location
        self.is_on = False  # Light starts OFF

    def toggle(self):
        self.is_on = not self.is_on  # Switch state

    def status(self):
        if self.is_on:
            print("ON")
        else:
            print("OFF")


# Example usage
light = SmartLight("Kitchen")

light.status()   # OFF
light.toggle()
light.status()   # ON
