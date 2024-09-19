
try:
    print(10/1)
    print([1, 2, 3, 4[4]])
except Exception as e:
    print(f"Se ha producido un error: {e}")

#EXTRA

def process_params(parameters: list):
    print(parameters[2])

    process_params([1, 2, 3])