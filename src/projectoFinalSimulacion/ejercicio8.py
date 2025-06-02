from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation


class Person(Agent):
    STATES = ["S", "I", "R"]

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "S"

    def step(self):
        if self.state == "I":
            neighbors = self.model.grid.get_neighbors(self.pos, radius=1)
            for neighbor in neighbors:
                if neighbor.state == "S" and self.random.random() < 0.3:
                    neighbor.state = "I"
            if self.random.random() < 0.1:  # Probabilidad de recuperación
                self.state = "R"


class SIRModel(Model):
    def __init__(self, N, width, height):
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        # Crear agentes
        for i in range(N):
            p = Person(i, self)
            self.grid.place_agent(p, (self.random.randrange(width), self.random.randrange(height)))
            self.schedule.add(p)
        # Paciente cero
        self.schedule.agents[0].state = "I"


# Ejecución
model = SIRModel(100, 20, 20)
for _ in range(100):
    model.step()
