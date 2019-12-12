

def applies_to_rules(number):
    same = False
    digits = [int(d) for d in str(number)]
    for i in range(0, len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
        if digits[i] == digits[i+1]:
            same += 1
    return same


def applies_to_rules_2(number):
    same = False
    same_digits = {}
    digits = [int(d) for d in str(number)]
    for i in range(0, len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
        if digits[i] == digits[i+1]:
            if digits[i] not in same_digits:
                same_digits[digits[i]] = 2
            else:
                same_digits[digits[i]] += 1
            same += 1
    for key, val in same_digits.items():
        if val == 2:
            return True
    return False


def count_possible_passwords(range):
    count = 0
    for i in range:
        if applies_to_rules_2(i):
            count += 1
    return count

print(count_possible_passwords(range(240920, 789857)))
print(applies_to_rules_2(244456))