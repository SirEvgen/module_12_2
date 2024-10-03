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

    def test_run(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        result_name = []
        place = 0
        expected_result = {}
        expected_finishers = 3
        all_speed = [runner.speed for runner in result.values()]
        for runner in result.values():
            result_name.append(runner)
            for max_speed in all_speed:
                if runner.speed >= max_speed:
                    result_name += runner.name
            place += 1
            expected_result[place] = runner.name
        self.assertEqual(expected_result, result, False)
        self.assertTrue(expected_result == result, True)
        self.assertEqual(len(result.values()), expected_finishers)
        self.assertEqual(expected_result, result)
        """Можно было конечно перебрать все значения в словаре и с помощью метода __str__
        из класса Runner заменить их на читаемые, но получается громоздкий код, да и лишняя
        работа ни к чему"""
        self.all_results.update(expected_result)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)


if __name__ == '__main__':
    unittest.main()
