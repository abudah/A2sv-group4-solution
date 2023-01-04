import textwrap

def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(width=max_width)
    wordList=wrapper.wrap(text=string)
    return "\n".join(wordList)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)