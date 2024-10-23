def all_variants(text):
    n = len(text)
    for i in range(n):
        for y in range(i + 1, n + 1):
            yield text[i:y]


a = all_variants("abc")
for i in a:
    print(i)
