# Sliding window template — memorise this
window = []
s = []
left = 0
for right in range(len(s)):
    # 1. expand window — add s[right]
    window.add(s[right])

    # 2. shrink window — while condition violated
    while window is False:  
        # while window is invalid:
        window.remove(s[left])
        left += 1

    # 3. update answer
    ans = max(ans, right - left + 1)