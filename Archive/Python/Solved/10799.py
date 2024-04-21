iron_pipe = input()
current_pipe = 0
total_pipe = 0
for i in range(0, len(iron_pipe)-1):
    if iron_pipe[i] == "(":
        if iron_pipe[i + 1] == "(":
            current_pipe += 1
    else:
        if iron_pipe[i - 1] == "(":
            total_pipe += current_pipe
        elif iron_pipe[i + 1] == "(":
            total_pipe += 1
            current_pipe -= 1
        else:
            current_pipe -= 1
            total_pipe += 1
if current_pipe != 0:
    total_pipe += 1
print(total_pipe)
