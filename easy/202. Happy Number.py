def ishappy(n: int) -> bool:
    check_numbers = set()  
    curr = n  
    while curr != 1: 
        if curr in check_numbers:  
            return False  
        check_numbers.add(curr)
       # print(check_numbers)
        digits = [int(numb) for numb in str(curr)]
        print(digits)
        # Calcular la suma de los cuadrados de los dígitos
        curr = sum(numb*numb for numb in digits)
    return True  # Si se sale del bucle, entonces es un número feliz


print(ishappy(999999999999999999999999999))