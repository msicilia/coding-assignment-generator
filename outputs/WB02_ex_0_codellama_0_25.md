  The solution to this problem involves implementing a function named "force" which takes two arguments, mass and acceleration. The function returns the product of these two values.

Next, we need to write some test cases that will check the correctness of the function. Test cases are written in a separate module that is imported into the main program. We can use the `assert` statement to verify that the output of the function is correct. Here's an example test case:
```
import unittest

class ForceTests(unittest.TestCase):
    def test_force(self):
        self.assertEqual(force(10, 2), 20)

if __name__ == '__main__':
    unittest.main()
```
I hope this helps! Let me know if you have any further questions or concerns.