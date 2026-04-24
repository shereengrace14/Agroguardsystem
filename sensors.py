import random

def get_data():
    return {
        "temperature": random.randint(20, 40),
        "moisture": random.randint(0, 100)
    }
