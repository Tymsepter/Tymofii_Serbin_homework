class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_workers(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Only instances of Worker class can be added as workers")

    def remove_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.remove(worker)
        else:
            raise ValueError("Only instances of Worker class can be removed as workers")

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, workers):
        for worker in workers:
            if not isinstance(worker, Worker):
                raise ValueError("Only instances of Worker class can be added as workers")
        self._workers = workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
        else:
            raise ValueError("Worker's boss must be an instance of Boss class")


boss1 = Boss(1, "Fadi Ahmad", "Beetroot Academy")
boss2 = Boss(2, "Tetiana Pokotilova", "Beetroot Academy")

worker1 = Worker(1, "Tymofii Serbin", "Beetroot Academy", boss1)

print(worker1.boss.name)
