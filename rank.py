def make_data(n):
    return [(f"player{i:06d}", (i * 37) % 1000)
            for i in range(n)]

def solve(players):
    return sorted(players, key=lambda player: (-player[1], player[0]))


data = make_data(20_000)
small = [("Zoe", 80), ("Ana", 95), ("Bo", 80)]


assert solve(small) == [("Ana", 95), ("Bo", 80), ("Zoe", 80)]
assert solve([]) == []



print(solve(small))