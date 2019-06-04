# leetcode 692. Top K Frequent Words


# 2019-6-4, 至少是目前看来最合理的一个解法,copy from others, 应该有更好的方法处理
# to be finished, 可以尝试用partition的方式实现下
import heapq as hq
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        此处实现至少有两个不熟悉的知识点,
        一. 字符串的大小比较
        二. heapq, 并不熟悉
        """
        class Freq:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq
            def __lt__(self, other):
                if self.freq < other.freq:
                    return -1
                if self.freq == other.freq and self.word > other.word: #字母序小的优先级大
                    return -1
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        data = []
        for key, val in d.items():
            f = Freq(key, val)
            if (len(data) < k):
                hq.heappush(data, f)
            else:
                if data[0] < f:
                    hq.heappop(data)
                    hq.heappush(data, f)
        ans = []
        while(len(data)>0):
            ans.append(hq.heappop(data).word)
            
        return ans[::-1]

class Freq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        print(self.word)
        print(self.freq)
        if self.freq < other.freq:
            return -1
        if self.freq == other.freq and self.word > other.word: #字母序小的优先级大
            return -1


if __name__ == '__main__':
    a = Freq('a', 2)
    b = Freq('b', 3)
    print(a<b)
    print(bool(a<b))