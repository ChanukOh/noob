def solution(id_list, report, k):
    reporter = {user: set() for user in id_list}
    reported = {user: 0 for user in id_list}
    stop = set()
    stopper = {user: 0 for user in id_list}

    for r in report:
        sender, receiver = r.split()
        if receiver not in reporter[sender]:
            reporter[sender].add(receiver)
            reported[receiver] += 1

    for user, count in reported.items():
        if count >= k:
            stop.add(user)

    for user, reporters in reporter.items():
        stopper[user] = sum(1 for reporter in reporters if reporter in stop)

    return [stopper[user] for user in id_list]
