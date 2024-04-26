"""
Initially let R be the set of all requests, and let A be empty
While R is not yet empty
    Choose a request i ∈ R that has the smallest finishing time
    Add request i to A
    Delete all requests from R that are not compatible with request i
EndWhile
Return the set A as the set of accepted requests
"""

requests = [(1, 3), (2, 5), (3, 9), (6, 8), (7, 9), (8, 10)]
# ---
#  ----
#   -------
#      ---
#       ---
#         --
# 12345678910

a = []
while requests:
    i = min(requests, key=lambda x: x[1])
    a.append(i)
    requests = [j for j in requests if j[0] >= i[1]]
print(a)

