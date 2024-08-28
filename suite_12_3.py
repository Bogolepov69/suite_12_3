import unittest

def skip_if_frozen(test_func):
    def wrapper(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertEqual(2 * 2, 4)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Замораживает все тесты в этом классе

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertTrue(False, "Этот тест не должен выполняться.")

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertEqual(3, 3)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)