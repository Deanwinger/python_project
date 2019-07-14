# KMP 算法

'''
int KMP(char * t, char * p) 
{
	int i = 0; 
	int j = 0;

	while (i < strlen(t) && j < strlen(p))
	{
		if (j == -1 || t[i] == p[j]) 
		{
			i++;
           	j++;
		}
	 	else 
           		j = next[j];
    	}

    if (j == strlen(p))
       return i - j;
    else 
       return -1;
}

void getNext(char * p, int * next)
{
	next[0] = -1;
	int i = 0, j = -1;

	while (i < strlen(p))
	{
		if (j == -1 || p[i] == p[j])
		{
			++i;
			++j;
			next[i] = j;
		}	
		else
			j = next[j];
	}
}

讲解链接：https://www.zhihu.com/question/21923021/answer/281346746
'''

# 完美

def KMP(t, p, p_next):
    '''t 为目标(主)字符串, s 为模式字符串'''
    i = j = 0
    t_length = len(t)
    p_length = len(p)

    while i < t_length and j < p_length:
        if j == -1 or t[i] == p[j]:
            i += 1                                                                                                                              
            j += 1
        else:
            j = pnext[j]

    if j == p_length:
        return i - j
    else:
        return -1

def gen_pnext(p):
    n = len(p)
    pnext = [None] * n    
    pnext[0] = -1
    i = 0
    j = -1
    while i < n-1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            pnext[i] = j
        else:
            j = pnext[j]
    return pnext


if __name__ == "__main__":

    t = "aabababababbbbaababaaaababababbab"
    p = "abbab"

    t1 = "aabcbabcaabcabcaababcabbcaab"
    p1 = "abcaababc"

    p2 = "abcabcaaa"
    t2 = "abcabcaababcaababcabbabbcabcabcaaabccabccab"

    s = 'ababababca'
    l =   'abababca'

    t2 = "ab"
    p2 = "ab"

    print(len(t2))
    pnext = gen_pnext(t2)
    print(pnext)

    print(KMP(t2, p2, pnext))