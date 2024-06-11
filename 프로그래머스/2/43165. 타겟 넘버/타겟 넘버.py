graph={}
for i in range(1,51):
    graph[i]=[i,-i]

def solution(numbers, target):
    
    def finder(numbers, found=None):
        if found is None:
            found = []

        if not numbers:
            return found

        current_digit = numbers[0]
        if current_digit in graph:
            new_found = []
            for letter in graph[current_digit]:
                if not found:
                    new_found.append(letter)
                else:
                    for item in found:
                        new_found.append(item + letter)
            return finder(numbers[1:], new_found)
        else:
            return found
    return finder(numbers).count(target)
