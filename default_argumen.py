def say_hello(name):
    print(f"hello {name}")

say_hello("wafy")
say_hello("wafi")

def say_hello(name="ahmad"):
    print(f"hello {name}")

# Pemanggilan fungsi harus di luar
say_hello("wafy")
say_hello()

