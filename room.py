class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name


class LivingSpace(Room):

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
        self.room_type = 'LivingSpace'
        self.living_space_occupants = []


class Office(Room):

    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.room_type = 'Office'
        self.office_occupants = []

