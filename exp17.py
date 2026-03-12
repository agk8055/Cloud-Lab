import threading

def write_characters(data):
    with open('output_file1.txt', 'w') as f:
        for ch in data:
            if ch.isalpha():
                f.write(ch)
    print("Thread1:Character written to output_file1.txt")
def write_numbers(data):
    with open('output_file2.txt', 'w') as f:
        for ch in data:
            if ch.isdigit():
                f.write(ch)
    print("Thread2:Numbers written to output_file2.txt")
def write_special_characters(data):
    with open('output_file3.txt', 'w') as f:
        for ch in data:
            if not ch.isalnum() and not ch.isspace():
                f.write(ch)
    print("Thread3:Special Characters written to output_file3.txt")
with open('input_file.txt', 'r') as file:
    data = file.read()

t1 = threading.Thread(target=write_characters, args=(data,), name="Thread 1")
t2 = threading.Thread(target=write_numbers, args=(data,), name="Thread 2")
t3 = threading.Thread(target=write_special_characters, args=(data,), name="Thread 3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All threads have completed")