# Uses python3

def get_change(m):
    count = 0
    while m >=  10:
        m -= 10
        count += 1
    while m >= 5:
        m -= 5
        count += 1
    while m > 0:
        m -= 1
        count += 1
    return count

def main():
    m =int(input())
    print(get_change(m))

main()
