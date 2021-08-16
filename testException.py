import unittest

class MyException(Exception):
    pass

class SecondException(Exception):
    pass


def throw_ex(var):
    print("First test")
    if var == 12:
        raise MyException("Not A Valid Number")

    if var == 20:
        raise SecondException("Not Valid ......")

    else:
        return True


class TestException(unittest.TestCase):
    def test_sample(self):
        #self.assertRaises((MyException,SecondException), throw_ex, 12)

        with self.assertRaises(MyException,msg="Try again") as context:
            throw_ex(12)

        with self.assertRaises(SecondException,msg="Try again") as context2:
            throw_ex(20)

        print(context.exception)
        print(context2.exception)

        

if __name__ =='__main__':
    unittest.main()