with open ("sample.txt") as f1:
    with open ("s.txt","w") as f2:
        for line in f1:
            f2.write(line)

print("done")