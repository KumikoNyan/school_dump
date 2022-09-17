# Manual GCD (Why would you even do this?)

n_val = int(input("N: "))
m_val = int(input("M: "))

min_val = min(n_val, m_val)

while (n_val % min_val) != 0 or (m_val % min_val) != 0:
    min_val = min_val - 1
print("GCD: " + str(min_val))