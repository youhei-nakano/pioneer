"""Finite exact subset-sum checks; no network or filesystem writes."""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
import json


def subset_sums(weights):
    result = [Fraction(0)]
    for weight in weights:
        result += [value + weight for value in result]
    return sorted(result)


def recover(spectrum):
    pending = Counter(spectrum)
    if pending[0] < 1:
        raise ValueError("missing empty subset")
    pending[0] -= 1
    pending += Counter()  # remove zero counts
    known = [Fraction(0)]
    result = []
    while pending:
        weight = min(pending)
        if weight <= 0:
            raise ValueError("strictly positive weights required")
        added = [value + weight for value in known]
        needed = Counter(added)
        if any(pending[value] < count for value, count in needed.items()):
            raise ValueError("inconsistent spectrum")
        pending.subtract(needed)
        pending += Counter()
        known += added
        result.append(weight)
    return result


def main():
    candidates = tuple(map(Fraction, ("1/3", "1/2", "2/3", "1", "3/2")))
    count = 0
    for length in range(8):
        for weights in combinations_with_replacement(candidates, length):
            assert recover(subset_sums(weights)) == list(weights)
            count += 1
    left = subset_sums((1, 3))
    right = subset_sums((2, 2))
    assert left != right and sum(left) == sum(right) == 8
    for invalid in ([0, 0], [0, 1, 3], [1, 2]):
        try:
            recover(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input accepted")
    result = {
        "passed": True,
        "positive_rational_lists_checked": count,
        "same_total_distinct_spectra": [[int(x) for x in left], [int(x) for x in right]],
        "invalid_inputs_rejected": 3,
        "limits": "Finite exact tests only; no geometric, A-infinity, or novelty claim.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
