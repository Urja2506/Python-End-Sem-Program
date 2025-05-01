def divide(numerator, denominator):
  try:
    result = numerator / denominator
    print(result)
    return result
  except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please provide a non-zero denominator.")
    return None
divide(10,0)
divide(10,2)

