
def recursive(i, n_terms, sign):
        
    if i >= n_terms:
        return 0
    current_term = sign / (2 * i + 1)
    
    return current_term + recursive(i + 1, n_terms, -sign)

pi_approx = 4 * recursive(0, 100, 1)
