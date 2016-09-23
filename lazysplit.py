def lazysplit(string, sep=None, maxsplit=-1):
    # TO DO: Different msg when maxsplit not a number and when maxsplit not an 
    # integral number.
    if not isinstance(maxsplit, int):
        raise TypeError()
    if sep is not None:
        if not isinstance(sep, str):
            raise TypeError(
                    "Can't convert '{}' object to str implicitly".format(
                        sep.__class__.__name__))
        if sep == '':
            raise ValueError('Empty separator') 
        # Run alg for given separator 
        word = []
        i = 0
        while i < len(string):
            if maxsplit == 0: 
                if string[i:]:
                    yield string[i:]
                return
            if string[i:i+len(sep)] == sep:
                yield ''.join(word)
                maxsplit -= 1
                word = []
                i += len(sep)
            else:
                word.append(string[i]) 
                i += 1
        yield ''.join(word)
    else:
        # Run algorithm for whitespaces
        word = []
        for i, char in enumerate(string):
            if maxsplit == 0: 
                if string[i:]:
                    yield string[i:].lstrip()
                return
            if char.isspace():
                if word:
                    yield ''.join(word)
                    maxsplit -= 1
                    word = []
                else:
                    continue
            else:
                word.append(char) 
        if word:
            yield ''.join(word)


class mystr(str):

    lazysplit = lazysplit
