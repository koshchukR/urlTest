def calculate_weighted_risk_score(scores):
    check1_weight = 0.5  # Check 1 has the highest weight
    check2_weight = 0.3  # Check 2 has medium weight
    check3_weight = 0.2  # Check 3 has the lowest weight

    weights = [check1_weight, check2_weight, check3_weight]
    weighted_scores = [score * weight for score, weight in zip(scores, weights)]
    overall_risk_score = sum(weighted_scores)

    return overall_risk_score
