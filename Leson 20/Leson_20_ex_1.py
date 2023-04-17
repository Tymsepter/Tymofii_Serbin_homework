import unittest
import leson18ex2


class TestBossAndWorkerClasses(unittest.TestCase):
    def setUp(self):
        self.boss1 = leson18ex2.Boss(1, "Fadi Ahmad", "Beetroot Academy")
        self.boss2 = leson18ex2.Boss(2, "Tetiana Pokotilova", "Beetroot Academy")
        self.worker1 = leson18ex2.Worker(1, "Tymofii Serbin", "Beetroot Academy", self.boss1)
        self.worker2 = leson18ex2.Worker(2, "John Doe", "Some Company", self.boss2)

    def test_worker_has_correct_boss(self):
        self.assertEqual(self.worker1.boss, self.boss1)
        self.assertEqual(self.worker2.boss, self.boss2)

    def test_add_worker_to_boss(self):
        self.boss1.add_workers(self.worker2)
        self.assertIn(self.worker2, self.boss1.workers)

    def test_remove_worker_from_boss(self):
        self.boss2.add_workers(self.worker1)
        self.boss2.add_workers(self.worker2)
        self.boss2.remove_worker(self.worker1)
        self.assertNotIn(self.worker1, self.boss2.workers)

    def test_add_non_worker_to_boss(self):
        with self.assertRaises(ValueError):
            self.boss1.add_workers("Not a worker")

    def test_remove_non_worker_from_boss(self):
        with self.assertRaises(ValueError):
            self.boss1.remove_worker("Not a worker")

    def test_set_worker_boss_with_non_boss_instance(self):
        with self.assertRaises(ValueError):
            self.worker1.boss = "Not a boss"


if __name__ == '__main__':
    unittest.main()