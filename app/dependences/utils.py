from app.models.user_models import UserBase
from typing import Generator
from datetime import datetime
import time


def fibonnaci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def userData(n) -> Generator[UserBase, None, None]:
    for i in range(n):
        yield UserBase(
            name=f"user {i}", email=f"user{i}@gmail.com", dateOfBirth=datetime.now()
        )


def calculateTime(func):
    def modifiedFunction(n):
        initTime = time.time()
        func(n)
        endTime = time.time()
        print(f"Execution Time { endTime - initTime} seconds")

    return modifiedFunction


@calculateTime
def imprimirNumeros(n):
    for i in range(n):
        print(i)
