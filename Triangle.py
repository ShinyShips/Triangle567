def classifyTriangle(a, b, c):
    '''
    Classify Triangle
    Classifies Triangles based on the given side lengths a, b, c
    Parameters:
    a (int): triangle side a
    b (int): triangle side b
    c (int): triangle side c

    requires that the input values be >= 0 and <= 200
    verifies that all 3 inputs are integers
    verifies that the sum of any 2 sides is greater than the third side
    Python's "isinstance(object,type) returns True if the object is of the specified type

    Returns:
    string: Type of Triangle or 'Not a Triangle' or 'Invalid Input'
    '''
    
    instance_list = [isinstance(a, int), isinstance(b, int), isinstance(c, int)]
    if (max(a, b, c) > 200 or min(a, b, c) < 0 or not instance_list):
        return 'Invalid Input'

    if ((a >= (b + c)) or (b >= (a + c)) or (c >= (a + b))):
        return 'Not A Triangle'

    if a == b and b == c:
        return 'Equilateral'
    elif ((((a ** 2) + (b ** 2)) == (c ** 2)) or
          (((a ** 2) + (c ** 2)) == (b ** 2)) or
          (((c ** 2) + (b ** 2)) == (a ** 2))):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    return 'Isoceles'
