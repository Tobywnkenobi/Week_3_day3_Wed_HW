def fibonacci(n, iteration=0, a=0, b=1):

    if iteration == n:
        return f"Iteration {iteration}: {b}"
    return f"Iteration {iteration}: {b}| " + fibonacci(n, iteration + 1,b, a + b)

answer = fibonacci(5)

print(answer)
