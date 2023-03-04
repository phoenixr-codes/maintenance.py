from maintenance import unstable

@unstable(until="0.1.0")
def divide(a: float, b: float) -> float:
    return a / b

if __name__ == "__main__":
    print(f"{divide(10, 8) = }")
