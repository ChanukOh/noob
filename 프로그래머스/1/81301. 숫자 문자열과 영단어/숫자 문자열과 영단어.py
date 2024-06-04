def solution(s):
    words_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    string = ''
    answer = ''
    for i in s:
        if i.isdigit():
            answer += i
            string = ''
        else:
            string += i
            if string in words_dict:
                answer += words_dict[string]
                string = ''
    return int(answer)

