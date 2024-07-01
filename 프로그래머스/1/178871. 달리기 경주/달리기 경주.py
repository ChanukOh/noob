def solution(players, callings):
    player_indices = {name: idx for idx, name in enumerate(players)}
    for name in callings:
        idx = player_indices[name]
        if idx > 0:
            players[idx], players[idx - 1] = players[idx - 1], players[idx]
            player_indices[players[idx]] = idx
            player_indices[players[idx - 1]] = idx - 1
    return players