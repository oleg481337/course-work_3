import funktion as funk

count_output = 0

operations = funk.create_ex_class()

for operation in operations:
    if operation.state == 'EXECUTED':
        funk.beautiful_result(operation)
        count_output += 1
    if count_output == 5:
        break
