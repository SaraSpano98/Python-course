# Any function that contains a yield statement returns a generator.
# Generators and iterators are interchangeable.

def count(start, step):
    while True:
        yield start
        start += step

counter = count(10, 2)
print(next(counter), next(counter), next(counter))
(10, 12, 14)