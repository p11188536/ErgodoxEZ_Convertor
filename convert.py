# import sys


# def swap(lst, i, j):
#     """Helper function to mimic the C++ swap logic."""
#     lst[i], lst[j] = lst[j], lst[i]


# def main():
#     # Check for command line arguments
#     if len(sys.argv) < 2:
#         print("invalid input!", file=sys.stderr)
#         sys.exit(-1)

#     input_filename = sys.argv[1]

#     # Read the initial file content
#     try:
#         with open(input_filename, "r") as inf:
#             lines = inf.readlines()
#     except IOError:
#         print("Can't open file!", file=sys.stderr)
#         sys.exit(-1)

#     keys = []
#     num = 0

#     # First Pass: Extract key layouts
#     for line in lines:
#         line_str = line.rstrip("\r\n")
#         pos = line_str.find("LAYOUT_ergodox")

#         if pos != -1:
#             pos += 15
#             current_pos = pos
#             row_keys = []

#             for i in range(76):
#                 np = line_str.find(",", current_pos)
#                 if np != -1:
#                     if i != 75:
#                         item = line_str[current_pos:np]
#                     else:
#                         item = line_str[current_pos : np - 1]
#                     row_keys.append(item)
#                     current_pos = np + 1
#                 else:
#                     print("Wrong!", file=sys.stderr)
#                     sys.exit(-1)

#             keys.append(row_keys)
#             num += 1
#             if num == 3:
#                 break

#     # Perform the layout swaps (mirrors left/right halves of the Ergodox layout)
#     for i in range(len(keys)):
#         # Rows 1-5 mirroring
#         for k in range(7):
#             swap(keys[i], k, 44 - k)
#         for k in range(7):
#             swap(keys[i], 7 + k, 51 - k)
#         for k in range(6):
#             swap(keys[i], 14 + k, 57 - k)
#         for k in range(7):
#             swap(keys[i], 20 + k, 64 - k)
#         for k in range(5):
#             swap(keys[i], 27 + k, 69 - k)

#         # Thumb cluster mirroring
#         swap(keys[i], 32, 71)
#         swap(keys[i], 33, 70)
#         swap(keys[i], 34, 72)
#         swap(keys[i], 35, 75)
#         swap(keys[i], 36, 74)
#         swap(keys[i], 37, 73)

#     # Second Pass: Reconstruct and write out to keymap.c
#     try:
#         with open("keymap.c", "w") as of:
#             num = 0
#             for line in lines:
#                 line_str = line.rstrip("\r\n")
#                 pos = line_str.find("LAYOUT_ergodox")

#                 if pos == -1 or num >= len(keys):
#                     of.write(line_str + "\n")
#                 else:
#                     pos += 15
#                     out_line = line_str[:pos]

#                     for i in range(76):
#                         out_line += keys[num][i]
#                         if i != 75:
#                             out_line += ","
#                         else:
#                             out_line += "),"

#                     of.write(out_line + "\n")
#                     num += 1
#     except IOError:
#         print("Can't write to file!", file=sys.stderr)
#         sys.exit(-1)

#     print("done!")


# if __name__ == "__main__":
#     main()