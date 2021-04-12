def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    idx, count = 0, 0

    if ruleKey == "type":
        idx = 0
    elif ruleKey == "color":
        idx = 1
    elif ruleKey == "name":
        idx = 2

    for item in items:
        if item[idx] == ruleValue:
            count += 1

    return count