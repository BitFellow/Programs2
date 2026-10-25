# Find-S Algorithm
data = [
    [">=9", "Yes", "Good", "Good", "Yes"],
    [">=8", "Yes", "Good", "Moderate", "Yes"],
    [">=9", "No", "Good", "Good", "No"],
    [">=8", "Yes", "Good", "Good", "Yes"]
]

h = None
for example in data:

    if example[-1] == "Yes":

        if h is None:
            h = example[:-1]

        else:
            for j in range(len(h)):
                if h[j] != example[j]:
                    h[j] = '?'

print("Final Hypothesis:", h)

# Candidate Elimination Algorithm
data = [
    [">=9", "Yes", "Good", "Good", "Yes"],
    [">=8", "Yes", "Good", "Moderate", "Yes"],
    [">=9", "No", "Good", "Good", "No"],
    [">=8", "Yes", "Good", "Good", "Yes"]
]

# Initial S and G
S = ['0', '0', '0', '0']
G = ['?', '?', '?', '?']

for example in data:

    x = example[:-1]
    target = example[-1]

    if target == "Yes":

        # Update S using positive example
        for i in range(4):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'

    else:

        # Update G using negative example
        for i in range(4):
            if G[i] == '?':
                G[i] = x[i]

    print("Example:", example)
    print("S =", S)
    print("G =", G)
    print()

print("Final S =", S)
print("Final G =", G)