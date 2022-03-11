import re

K = 4
N = 10

with open('text.txt') as open_file:
    s = open_file.read()


def FrequencyList(s: str) -> list:
    cnt = {}
    for i in re.sub('[^\w\s]', ' ', s.lower().replace('\n', ' ')).split(' '):
        if len(i) > 0:
            cnt.setdefault(i, 0)
            cnt[i] += 1
    return sorted(cnt.items(), key=lambda item: item[1])


def WordsCounts(s: str) -> list:
    cnt = []
    for p in re.sub('[!?]', '.', s).split('.'):
        words = 0
        for i in p.split(' '):
            if len(i) > 0:
                words += 1
        if words > 0:
            cnt += [words]
    return cnt


def Average(cnt: list):
    return sum(cnt) / len(cnt)


def Median(cnt: list):
    cnt = sorted(cnt)
    return (cnt[len(cnt) // 2] + cnt[(len(cnt) - 1) // 2]) / 2


def Ngramms(s: str, K: int) -> str:
    cnt = {}
    s = re.sub('[^a-z]', '', s.lower())
    for i in range(len(s) - K + 1):
        subs = s[i:i + K]
        cnt.setdefault(subs, 0)
        cnt[subs] += 1
    return sorted(cnt.items(), key=lambda item: item[1], reverse=True)


print(FrequencyList(s))
print("Average amount of words in sentence:", Average(WordsCounts(s)))
print("Median amount of words in sentence:", Median(WordsCounts(s)))
dct = Ngramms(s, K)
print(f"Top-{N} {K}-gramms:")
print([dct[i] for i in range(min(N, len(dct)))])
