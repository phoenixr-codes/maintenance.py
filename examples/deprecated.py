from maintenance import deprecated

@deprecated(since="0.1.0", new="divide")
def div(a: float, b: float) -> float:
    return divide(a, b)

def divide(a: float, b: float) -> float:
    return a / b

if __name__ == "__main__":
    print(f"{div(10, 8) = }")
    print(div.__doc__)
