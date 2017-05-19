import person
import room
import sqlite3


class Amity(object):
    def __init__(self):
        self.offices = []
        self.living_spaces = []
        self.all_people_in_amity = []
        self.all_people_in_amity_with_out_room_allocations = []
        self.all_rooms_in_amity = []

        self.offices_names = []
        self.living_spaces_names = []
        self.all_people_names_in_amity = []
        self.all_people_names_in_amity_with_out_room_allocations = []
        self.every_room_in_amity = self.offices_names + self.living_spaces_names

    def create_office(self, room_name, room_type):
        """creating an office and adding it to office list"""

        office = room.Office(room_name)

        if isinstance(room_name, str) == True:
            if (office.room_type == room_type) is True:
                self.offices.append(office)

                return 'An %s has been created.' % self.offices[0].room_type

            else:
                return 'Invalid room type for office!'
                # tried doing some recussion here but the code cant be reached, need some help on that.

        else:
            return '%s is not a string' % room_name

    def create_living_space(self, room_name, room_type):
        """creating a living space and adding it to living space list"""

        living_spaces = room.LivingSpace(room_name)
        if (living_spaces.room_type == room_type) is True:
            self.living_spaces.append(living_spaces)

            return 'a %s has been created.' % self.living_spaces[0].room_type

        else:
            return 'Invalid room type!'

    def add_staff(self, first_name, second_name, person_type):
        """creating and adding  staff to an office"""

        new_staff = person.Staff(first_name, second_name, person_type)
        for an_office in self.offices:
            space_available = len(an_office.office_occupants)
            if space_available < 7:
                an_office.office_occupants.append(new_staff)
                self.all_people_in_amity.append(new_staff)

                return '%s has been assigned an office as staff.' % new_staff.person_name

            else:
                self.all_people_in_amity_with_out_room_allocations.append(new_staff)

                return 'No offices available at the moment'

    def add_fellow(self, first_name, second_name, person_type):
        """creating and adding a fellow to an office"""

        new_fellow = person.Fellow(first_name, second_name, person_type)
        for an_office in self.offices:
            space = len(an_office.office_occupants)
            if space < 7:
                an_office.office_occupants.append(new_fellow)
                self.all_people_in_amity.append(new_fellow)
                # self.assign_living_space_option() --> call to class property above

                print ('Hey %s you have been assigned %s as your office, would you want a living space?'
                       ',' % (new_fellow.first_name, an_office.room_name))
                living_space_answer = raw_input('Y/N: ')
                if living_space_answer.upper() == 'Y':
                    return self.assign_living_space_to_fellow(new_fellow.person_name)

                else:
                    return '%s has been assigned an office as a fellow.' % new_fellow.person_name

                # return '%s has been assigned an office as a fellow.' % new_fellow.person_name

            else:
                # if an empty room is not available for assignment, the person is added to the this list
                self.all_people_in_amity_with_out_room_allocations.append(new_fellow)

                return 'No offices available at the moment!'

    '''need help on this one too'''

    def display_people_in_room(self, room_name):
        for single_office in self.offices:
            if single_office.room_name == room_name:
                occupants_in_office = single_office.office_occupants
                current_office_occupants = []
                for occupant in occupants_in_office:
                    current_office_occupants.append(occupant.person_name)
                return current_office_occupants
            else:
                return '%s does not exist, please try a room that exists, Thank you!' % room_name

    def print_unallocated_people(self):
        """returning all people who haven't been allocated rooms"""

        return self.all_people_in_amity_with_out_room_allocations

    def all_the_rooms_in_amity(self):
        """this method returns all rooms available in Amity"""

        # iterating through the offices list and appending the room name value to the all rooms list
        for i in self.offices:
            self.all_rooms_in_amity.append(i)

        # iterating through the living spaces list and appending the room name value to the all rooms list
        for j in self.living_spaces:
            self.all_rooms_in_amity.append(j)

        # returning all room names stored in the all rooms list.
        return 'There is %s rooms in Amity.' % len(self.all_rooms_in_amity)

    def print_allocations(self):
        """printing all rooms and people in those respective rooms"""

        rooms_and_people_in_them_rooms = {}

        for self.every_room in self.all_rooms_in_amity:
            room_name_is = self.every_room.room_name

            if self.every_room.room_type == 'Office':
                people_objects_in_office = self.every_room.office_occupants

                names_of_people_in_the_office = []
                for every_person in people_objects_in_office:
                    names_of_people_in_the_office.append(every_person.person_name)

                rooms_and_people_in_them_rooms[room_name_is] = names_of_people_in_the_office

            elif self.every_room.room_type == 'LivingSpace':
                people_objects_in_living_space = self.every_room.living_space_occupants

                names_of_people_in_living_space = []
                for every_person in people_objects_in_living_space:
                    names_of_people_in_living_space.append(every_person)

                rooms_and_people_in_them_rooms[room_name_is] = names_of_people_in_living_space

        return rooms_and_people_in_them_rooms

    def all_the_people_in_amity(self):

        all_people_in_amity_names = []
        for i in self.all_people_in_amity:
            all_people_in_amity_names.append(i.person_name)

        return all_people_in_amity_names

    '''def save_state(self):

        for i in self.offices:
            self.offices_names.append(i.room_name)

        for j in self.living_spaces:
            self.living_spaces_names.append(j.room_name)

        for k in self.all_people_in_amity:
            self.all_people_names_in_amity.append(k.person_name)

        for l in self.all_people_names_in_amity_with_out_room_allocations:
            self.all_people_names_in_amity_with_out_room_allocations.append(l.person_name)'''

    def assign_living_space_to_fellow(self, fellow_full_name):

        for a_living_space in self.living_spaces:
            space = len(a_living_space.living_space_occupants)
            if space < 5:
                a_living_space.living_space_occupants.append(fellow_full_name)

                return ('%s you have been assigned %s as your living space' % (fellow_full_name, a_living_space.room_name))

            else:
                self.all_people_in_amity_with_out_room_allocations.append(fellow_full_name)
                return ('No living spaces available at the moment!')


'''
    def reallocate(self, first_name, second_name, room_name):

        # i want to do it this way: serach if the name exists, if it does, then i locate where i stored it, 
        # then i delete it from the old list or room, and then i assign it to a new room by calling the allocate room, 
        # method.
        full_person_name = '%s %s' % (first_name, second_name)
        persons_name = []
        for i in self.all_people_in_amity:
            persons_name.append(i.person_name)

        if full_person_name in persons_name:
                

        else:
            print ('bigaanye okukola')



    def load_people(self):
        pass

    def save_state(self):
        pass

    def load_state(self):
        pass
'''
new_amity = Amity()

print(new_amity.create_office('mordor', 'Office'))

print(new_amity.create_living_space('st. catherine', 'LivingSpace'))

print(new_amity.add_staff('David', 'Mukiibi', 'Staff'))

print(new_amity.add_fellow('Timothy', 'Wikedzi', 'Fellow'))

print (new_amity.print_unallocated_people())

print (new_amity.all_the_rooms_in_amity())

print (new_amity.print_allocations())

print (new_amity.all_the_people_in_amity())

#print (new_amity.save_state())



# print(new_amity.display_people_in_room('narnia'))

# print(new_amity.pipo_in_an_office())
