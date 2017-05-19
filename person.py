import uuid


class Person(object):

    def __init__(self, first_name, second_name,  person_type):
        self.first_name = first_name
        self.second_name = second_name
        self.person_name = '%s %s' % (self.first_name,  self.second_name)
        self.person_type = person_type



class Staff(Person):

    def __init__(self, first_name, second_name, person_type):
        super(Staff, self).__init__(first_name, second_name, person_type)


class Fellow(Person):

    def __init__(self, first_name, second_name, person_type):
        super(Fellow, self).__init__(first_name, second_name, person_type)
