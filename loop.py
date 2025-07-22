for j in range(5):
    for i in range(5):
        print(f"i: {i}, j: {j}")
        if i == 2 and j == 3:
            break
    else:
        continue
    break