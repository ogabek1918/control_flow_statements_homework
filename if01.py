def main(a):
    """
    If the number is positive, increase it to 1,otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    s=0
    b=1
    if a>0:
       s=a+b
    if a<0:
       s = a
    return s
print(main(1))
