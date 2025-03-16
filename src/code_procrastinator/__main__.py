import code_procrastinator.procrastinator as procrastinator

def main():
    @procrastinator.excuse_wrapper
    def add(x, y):
        return x + y
    print(add(1, 2))
    

if __name__ == "__main__":
    main()