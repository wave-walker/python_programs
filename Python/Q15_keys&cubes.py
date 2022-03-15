def generate_dict(num):
    return {num:num**3 for num in range(1,num+1)} # will print a dict where the keys are numbers and the values are cubes of the keys.

print(generate_dict(5)) #number input to generate from 1-5