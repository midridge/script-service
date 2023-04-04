from typing import Tuple

def add(a: float, b: float) -> Tuple[float, ...]:
    return a + b, a - b

result = add(**kwargs)