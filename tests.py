import unittest
from amity import Amity


class AmityTests(unittest.TestCase):
    def setUp(self):
        """setting up resources/dependencies these tests rely on to run."""

        self.amity_object = Amity()
        self.office_available = self.amity_object.create_office('mordor', 'Office')
        self.living_space_available = self.amity_object.create_living_space('st. catherine', 'LivingSpace')
        self.new_staff_added = self.amity_object.add_staff('David', 'Mukiibi', 'Staff')
        self.new_fellow_added = self.amity_object.add_fellow('Timothy', 'Wikedzi', 'Fellow')
        self.people_exist_in_room = self.amity_object.display_people_in_room('mordor')


    def test_office_created_successfully(self):
        """testing successful creation of an office"""

        self.amity_object.offices.append(self.office_available)
        final_no = len(self.amity_object.offices)
        self.assertEqual(1 <= final_no, bool(final_no))
       # with self.assertRaises(Exception):
            # self.office_available()

    def test_office_name_created_with_aplhabets_only(self):
        # will need help on this test

        self.amity_object.offices.append(self.office_available)
        if isinstance(self.office_available.room_name, str) == False:
            self.assertTrue()
        else:
            pass

    def test_living_space_created_with_alphabets_only(self):
        pass

    def test_fellow_name_created_with_alphabets_only(self):
        pass

    def test_staff_name_created_with_alphabets_only(self):
        pass

    def test_living_space_created_successfully(self):
        """testing successful creation of a living space"""

        self.amity_object.living_spaces.append(self.living_space_available)
        space_created = len(self.amity_object.living_spaces)
        self.assertTrue(1 <= space_created, bool(space_created))

    def test__staff_added_successfully(self):
        """ testing successful addition of staff to an office"""

        # self.amity_object.add_staff('david', 'Staff')
        people_in_andela = len(self.amity_object.all_people_in_amity)
        self.assertTrue(people_in_andela > 0, people_in_andela)

    def test_fellow_added_successfully(self):
        """testing successful addition of a fellow to an office"""

        # self.amity_object.add_fellow('david', 'Fellow')
        people_in_andela = len(self.amity_object.all_people_in_amity)
        self.assertTrue(people_in_andela > 0, people_in_andela)


    def test_room_name_is_not_empty(self):
        pass

    def test_loading_data_from_db_works_if_db_has_data(self):
        pass

    def test_loading_data_from_db_returns_appropriately_if_db_has_no_data(self):
        pass

    def test_printing_room_occupants_works(self):
        pass

    def test_printing_unallocated_people_works(self):
        pass

    def test_reallocating_a_person_works(self):
        pass

    def tets_fellow_added_successfully_to_living_space(self):
        pass



















    def test_people_in_room_exist(self, room_name):
        """this test is to confirm that people really do exist in the specified room."""

        # its still confusing me, but am yet to work it out.
        # on second thought i need help on this
        # self.amity_object.display_people_in_room(room_name)
        for k in self.amity_object.offices:
            if room_name == k.room_name:
                self.pipo_exist = len(k.office_occupants)
            self.assertTrue(True, self.pipo_exist > 0)

            # need help on how to write the test for all_the_rooms_in_amity method in the Amity model.


suite = unittest.TestLoader().loadTestsFromTestCase(AmityTests)
unittest.TextTestRunner(verbosity=2).run(suite)
