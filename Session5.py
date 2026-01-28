import math

def main():
    start = 0.0
    end = 2.0
    num_points = 1000

    step = (end - start) / (num_points - 1)

    print("      x\t\t sin(x)")
    print("______________________________________")

    for i in range(num_points):
        x = start + i * step
        y = math.sin(x)
        print(f"{x:.6f}\t {y:.6f}")


# Program entry point
if __name__ == "__main__":
    main()
