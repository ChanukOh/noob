def solution(N, stages):
    total_players = [0] * (N + 2) 
    for stage in stages:
        total_players[stage] += 1
    failure_rates = []
    num_players_on_stage = len(stages)
    for i in range(1, N + 1):
        if num_players_on_stage > 0:
            failure_rate = total_players[i] / num_players_on_stage
        else:
            failure_rate = 0
        failure_rates.append((i, failure_rate))
        num_players_on_stage -= total_players[i]
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    answer = [stage[0] for stage in failure_rates]
    return answer