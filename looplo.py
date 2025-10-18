def gcdOfStrings(str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
                print (len1, len2 = len2, len1 % len2) 
            return len1

        return str1[:gcd(len(str1), len(str2))]
# Example usage:

# sol = Solution()

print(gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"  