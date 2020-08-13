# python3

_multiplier = 263
_prime = 1610612741

def _hash_func(s):
        ans = 0
        for c in reversed(s):
            ans = (ans * _multiplier + ord(c)) % _prime
        return ans

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    res = []
    x = (_multiplier ** len(pattern)) % _prime
    tex = _hash_func(pattern)
    st = _hash_func(text[len(text)-len(pattern):])
    
    if st == tex and pattern  == text[len(text)-len(pattern):]:
        res.append(len(text)-len(pattern))
        
    for i in range(len(text)-len(pattern)-1,-1,-1):
        st = ((_multiplier * st) + ord(text[i]) - (x * ord(text[i+len(pattern)]))) % _prime
        if st == tex and pattern  == text[i:i+len(pattern)]:
            res.append(i)
    return reversed(res)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

