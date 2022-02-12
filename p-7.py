input = int(input())

def lap(str):
    if (str == str[::-1]):
        return True
    else:
            if (len(str) % 2 == 0):
              if str[:len(str) // 2] == str[len(str) // 2:]:
                return 1
              else:
                return 0

            else:
             if str[:len(str) // 2] == str[len(str) // 2 + 1:]:
                return 1
             else:
                return 0

for _ in range(input):
    print(lap(input("Enter: ")))