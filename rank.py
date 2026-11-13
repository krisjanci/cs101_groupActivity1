def make_data(n):
    return [(f"player{i:06d}", (i * 37) % 1000)
            for i in range(n)]

data = make_data(20_000)
# Also try make_data(40_000).


small = [("Zoe", 80), ("Ana", 95), ("Bo", 80)]
assert solve(small) == [("Ana", 95), ("Bo", 80), ("Zoe", 80)]
assert solve([]) == []