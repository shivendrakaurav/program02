import time, sys
from Sets import read_file, write_file, validate_args, intersection


if __name__ =="__main__":
    try:
        start = time.time()
        l1_file, l2_file, ret_file = validate_args(sys.argv)
        l1 = read_file(l1_file)
        l2 = read_file(l2_file)
        result = intersection(l1,l2)
        write_file(result,ret_file)

        end = time.time()
        print(f"Output: {l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {sys.argv[3]}: {len(result)} emails; Time taken: {int(end - start)} seconds")

    except Exception as e1:
        print("Generic error: {0}".format(e1))