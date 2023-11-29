def enter_vector(vector_name):
    try:
        n = int(input(f"Enter the dimension of the {vector_name} vector (n): "))
        if n < 1:
            raise ValueError("Dimension must be a positive integer.")
        
        vector = []
        for i in range(n):
            element = float(input(f"Enter the {i+1}-th element of the {vector_name} vector: "))
            vector.append(element)
        
        return vector
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Example usage:
vector_u = enter_vector("u")
vector_v = enter_vector("v")

if vector_u is not None and vector_v is not None:
    print("Entered vector u:", vector_u)
    print("Entered vector v:", vector_v)
