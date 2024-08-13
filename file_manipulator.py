import sys

def validateArgs():
    use_method = sys.argv[1]
    methods = {
        "reverse": 4,
        "copy": 4,
        "duplicate-contents": 5,
        "replace-string": 6
    }

    if len(sys.argv) != methods.get(use_method, 0):
        print("Wrong argument or usage name!")
        print_usage()
        sys.exit()

def print_usage():
    print("Usage:")
    print(" python3 file_manipulator.py reverse input.txt output.txt")
    print(" python3 file_manipulator.py copy input.txt output.txt")
    print(" python3 file_manipulator.py duplicate-contents input.txt output.txt num")
    print(" python3 file_manipulator.py replace-string input.txt output.txt needle new_string")

def reverse(contents): return contents[::-1]
def copy (contents): return contents
def duplicate_contents(contents, num): return contents * num
def replace_string(contents, needle, new_string): return contents.replace(needle, new_string) 

def main():
    validateArgs()
    use_method, input_file, output_file = sys.argv[1:4]

    with open(input_file) as input_f:
        contents = input_f.read()

    if use_method == "reverse":
        new_contents = reverse(contents)
    elif use_method == "copy":
        new_contents = copy(contents)
    elif use_method == "duplicate-contents":
        new_contents = duplicate_contents(contents, int(sys.argv[4]))
    elif use_method == "replace-string":
        new_contents = replace_string(contents, sys.argv[4], sys.argv[5])

    with open(output_file, 'w') as output_f:
        contents = output_f.write(new_contents)


if __name__ == "__main__":
    main()



# reverse inputpath outputpath: inputpath にあるファイルを受け取り、
#    outputpath に inputpath の内容を逆にした新しいファイルを作成します。

# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。

# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、
#   その内容を複製し、複製された内容を inputpath に n 回複製します。

# replace-string inputpath needle newstring: 
#   inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
