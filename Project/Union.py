import time,sys
from Sets import validate_args, Myset


if __name__ == "__main__":
    try:

        start = time.time()
        l1_file, l2_file, ret_file = validate_args(sys.argv)
        l1 = Myset(l1_file)
        l2 = Myset(l2_file)
        result = l1 | l2
        result.write_file(ret_file)
        end = time.time()

        print(f"Output: {l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {ret_file}: {len(result)} emails; Time taken: {int(end - start)} seconds")

    except Exception as e1:
        raise e1
        print("Generic error: {0}".format(e1))