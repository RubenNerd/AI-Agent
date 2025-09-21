from functions.get_files_info import get_files_info

def print_block(header, result):
    print(header)
    for line in result.splitlines():
        print(f"  {line}")

def main():
    print_block("Result for current directory:", get_files_info("calculator", "."))
    print_block("Result for 'pkg' directory:", get_files_info("calculator", "pkg"))
    print_block("Result for '/bin' directory:", get_files_info("calculator", "/bin"))
    print_block("Result for '../' directory:", get_files_info("calculator", "../"))

if __name__ == "__main__":
    main()