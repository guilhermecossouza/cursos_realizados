def fatorial(n):
    return (n * fatorial(n - 1) if n > 1 else 1)


if __name__ == "__main__":
    print(f"10!= {fatorial(10)}")

    # 6 semanas em segundos é igual ao fatorial de 10!
    print(6 * 7 * 24 * 60 * 60)
