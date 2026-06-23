class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)
        while read < n:
            cnt = 0
            char = chars[read]
            while read < n and char == chars[read]:
                read += 1
                cnt += 1
            chars[write] = char
            write += 1
            
            if cnt > 1:
                for c in str(cnt):
                    chars[write] = c
                    write += 1
        return write