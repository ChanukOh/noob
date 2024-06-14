def solution(score):
    average_scores = [(a + b) / 2 for a, b in score]

    sorted_scores = sorted(average_scores, reverse=True)

    ranks = []

    for avg in average_scores:
        rank = sorted_scores.index(avg) + 1
        ranks.append(rank)

    return ranks