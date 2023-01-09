import os


def f_findme(p: str):
    file_path = "/dir_test_1/dir_test_2/findme.txt"
    # runner_path = os.getcwd()
    path = os.path.normpath(p + file_path)
    print(f'PATH==> {path}')

    with open(file=path, mode='r') as r:
        x = r.read()
        print(x)
        r.close()
