import simpy
import random

# Contador para identificar a cada profesor
contador_profesores = 0


def profesor(env, ticket_counter, utensilios, bandeja, id_profesor):
    global contador_profesores
    tiempo_llegada = env.now
    print(f"\n[Tiempo {env.now:.2f}] Profesor {id_profesor} llega al comedor")

    # Proceso para comprar el ticket
    with ticket_counter.request() as solicitud:
        print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} EN COLA para comprar ticket")
        yield solicitud
        print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} INICIA compra de ticket")
        tiempo_compra = random.uniform(1, 3)
        yield env.timeout(tiempo_compra)
        print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} TERMINA compra de ticket (duró {tiempo_compra:.2f} min)")

    # Decisión de tomar utensilios
    if random.random() < 0.8:
        with utensilios.request() as solicitud:
            print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} EN COLA para utensilios")
            yield solicitud
            print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} INICIA toma de utensilios")
            tiempo_utensilios = random.uniform(0, 1.5)
            yield env.timeout(tiempo_utensilios)
            print(
                f"[Tiempo {env.now:.2f}] Profesor {id_profesor} TERMINA utensilios (duró {tiempo_utensilios:.2f} min)")
    else:
        print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} NO toma utensilios")

    # Proceso para tomar la bandeja
    with bandeja.request() as solicitud:
        print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} EN COLA para bandeja")
        yield solicitud
        print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} INICIA llenado de bandeja")
        tiempo_bandeja = random.uniform(0.5, 1.5)
        yield env.timeout(tiempo_bandeja)
        print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} TERMINA bandeja (duró {tiempo_bandeja:.2f} min)")

    # Área de comer
    print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} INICIA a comer")
    tiempo_comer = random.uniform(10, 20)
    yield env.timeout(tiempo_comer)
    print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} TERMINA de comer (duró {tiempo_comer:.2f} min)")

    # Salida
    print(f"[Tiempo {env.now:.2f}] Profesor {id_profesor} SALE del comedor\n")


def generador_profesores(env, ticket_counter, utensilios, bandeja):
    global contador_profesores
    while True:
        yield env.timeout(random.expovariate(1 / 0.5))
        contador_profesores += 1
        env.process(profesor(env, ticket_counter, utensilios, bandeja, contador_profesores))


# Configuración
env = simpy.Environment()
ticket_counter = simpy.Resource(env, capacity=1)
utensilios = simpy.Resource(env, capacity=1)
bandeja = simpy.Resource(env, capacity=1)

env.process(generador_profesores(env, ticket_counter, utensilios, bandeja))
env.run(until=30)  # Simulación más corta para ejemplo (1 .. n)
