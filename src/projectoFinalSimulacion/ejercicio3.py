import simpy
import random


class Persona:
    def __init__(self, env, id, estado_inicial="S"):
        self.env = env
        self.id = id
        self.estado = estado_inicial

    def infectar(self):
        if self.estado == "S" and random.random() < 0.3:  # 30% de probabilidad
            self.estado = "I"
            print(f"Persona {self.id} infectada en t={self.env.now}")
            yield self.env.timeout(14)  # Tiempo de recuperación
            self.estado = "R"


def simulacion(env, num_personas=100):
    personas = [Persona(env, i) for i in range(num_personas)]
    personas[0].estado = "I"  # Paciente cero

    while True:
        for persona in personas:
            if persona.estado == "I":
                # Infectar a vecinos cercanos
                vecinos = random.sample(personas, 5)
                for vecino in vecinos:
                    env.process(vecino.infectar())
        yield env.timeout(1)  # Paso de tiempo
        for persona in personas:
            print(f"Persona {persona.id}: {persona.estado}")


env = simpy.Environment()
env.process(simulacion(env))
env.run(until=30)
