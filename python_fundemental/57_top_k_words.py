# leetcode 692. Top K Frequent Words


# 2019-6-4, 至少是目前看来最合理的一个解法,copy from others, 下面的这个解法最关键的其实
# 就是那个Freq类, 比较大小的处理,非常的clever
# to be finished, 可以尝试用partition的方式实现下
import heapq as hq
class Solution:
    def topKFrequent(self, words, k: int):
        class Freq:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq
            def __lt__(self, other):
                if self.freq < other.freq:
                    return True
                if self.freq == other.freq and self.word > other.word: #字母序小的优先级大
                    return True
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        data = []
        for key, val in d.items():
            print(key)
            f = Freq(key, val)
            if (len(data) < k):
                hq.heappush(data, f)
            else:
                print("top is: ", data[0].word)
                print("f is: ", f.word)
                if data[0] < f:

                    hq.heappop(data)
                    hq.heappush(data, f)
        ans = []
        while(len(data)>0):
            ans.append(hq.heappop(data).word)
            
        return ans[::-1]

# class Freq:
#     def __init__(self, word, freq):
#         self.word = word
#         self.freq = freq
#     def __lt__(self, other):
#         print(self.word)
#         print(self.freq)
#         if self.freq < other.freq:
#             return -1
#         if self.freq == other.freq and self.word > other.word: #字母序小的优先级大
#             return -1


if __name__ == '__main__':
    # a = Freq('a', 2)
    # b = Freq('b', 3)
    # print(a<b)
    # print(bool(a<b))
    word = ["lov", "love", "leetcode", "lov", "love", "coding"]
    k = 1
    s = Solution()
    print(s.topKFrequent(word, k))