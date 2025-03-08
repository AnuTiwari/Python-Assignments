class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

def main():
    s1 = input("Enter first string: ").strip()
    s2 = input("Enter second string: ").strip()

    solution = Solution()  # Creating an instance of the class
    if solution.isAnagram(s1, s2):
        print("Anagram")
    else:
        print("Not an Anagram")

if __name__ == "__main__":
    main()
