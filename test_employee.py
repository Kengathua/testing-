import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')


    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('John','Oruko',600000)
        self.emp_2 = Employee('Jane', 'Atieno', 500000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'John.Oruko@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Atieno@email.com')

        self.emp_1.first = 'Moses'
        self.emp_2.first = 'Rahab'

        self.assertEqual(self.emp_1.email,'Moses.Oruko@email.com')
        self.assertEqual(self.emp_2.email,'Rahab.Atieno@email.com') 
    

    def test_fullname(self):
        print('test_fullname')
        emp_1 = Employee('John','Oruko',500000)
        emp_2 = Employee('Jane', 'Atieno', 500000)

        self.assertEqual(emp_1.fullname, 'John Oruko')
        self.assertEqual(emp_2.fullname, 'Jane Atieno')

        emp_1.first = 'Moses'
        emp_2.first = 'Rahab'

        self.assertEqual(emp_1.fullname,'Moses Oruko')
        self.assertEqual(emp_2.fullname,'Rahab Atieno') 

    def test_apply_raises(self):
        print('test_apply_raises')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,630000)
        self.assertEqual(self.emp_2.pay,525000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_once_with('http://company.com/Oruko/May')

            self.assertEqual(schedule, 'Success')





    if __name__ == '__main__':
        unittest.main()