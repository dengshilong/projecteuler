MAX = '1' * 500

passcode = {}


def find_passcode(items):
    items = set(items)
    if len(items) == 0:
        return ''
    t = list(items)
    t.sort()
    key = ','.join(t)
    if key in passcode:
        return passcode[key]
    result = MAX
    s = set()
    for item in items:
        s.add(item[0])
    for c in s:
        x = set()
        for item in items:
            if item[0] == c:
                t = item[1:]
                if t:
                    x.add(t)
            else:
                x.add(item)
        temp = c + find_passcode(x)
        if len(temp) < len(result):
            result = temp
    passcode[key] = result
    return result


if __name__ == "__main__":
    with open("pe79.txt") as f:
        items = [line.strip() for line in f]
        print(find_passcode(items))