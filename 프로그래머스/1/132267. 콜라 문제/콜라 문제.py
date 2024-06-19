def solution(a, b, n):
    total_bottles = n
    total_cola_bottles = 0
    
    while total_bottles >= a:
        received_colas = total_bottles // a
        total_cola_bottles += received_colas * b
        total_bottles = total_bottles % a + received_colas * b
    
    return total_cola_bottles