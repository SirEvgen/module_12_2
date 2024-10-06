import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.result = tournament.start()
        result_name = []
        place = 0
        self.expected_result = {}
        self.expected_finishers = 3

        for runner in self.result.values():
            result_name.append(runner)

            place += 1
            self.expected_result[place] = runner.name

    def test_run(self):
        self.assertEqual(self.expected_result, self.result)
        """Можно было конечно перебрать все значения в словаре и с помощью метода __str__
        из класса Runner заменить их на читаемые, но получается громоздкий код, да и лишняя
        работа ни к чему"""
        self.all_results.update(self.expected_result)

    def test_inequality(self):
        self.assertEqual(self.expected_result, self.result, False)

    def test_equality(self):
        self.assertTrue(self.expected_result == self.result, True)

    def test_finishers(self):
        self.assertEqual(len(self.result.values()), self.expected_finishers)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)


if __name__ == '__main__':
    unittest.main()
