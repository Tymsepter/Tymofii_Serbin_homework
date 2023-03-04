CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channel):
        self.channels = channel
        self.current_channels_index = 0

    def first_channel(self):
        self.current_channels_index = 0
        return self.channels[0]

    def last_channel(self):
        self.current_channels_index = len(self.channels) - 1
        return self.channels[-1]

    def turn_channel(self, n):
        if n < 1 or n > len(self.channels):
            return None
        self.current_channels_index = n - 1
        return self.channels[self.current_channels_index]

    def next_channel(self):
        self.current_channels_index = (self.current_channels_index + 1) % len(self.channels)
        return self.channels[self.current_channels_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channels_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def is_exist(self, channel):
        if isinstance(channel, int):
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        else:
            return "Yes" if channel in self.channels else "No"


controller = TVController(CHANNELS)

print(controller.first_channel())

print(controller.last_channel())

print(controller.turn_channel(1))

print(controller.next_channel())

print(controller.previous_channel())

print(controller.current_channel())

print((controller.is_exist(4)))

print(controller.is_exist("BBC"))
