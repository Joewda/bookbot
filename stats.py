def word_count(booktext):
    if booktext == "":
        print("ERROR: blank text")
        return 0
    else:
        count=0

        count = len(booktext.split())
        return count
    
def char_count(booktext):
    booktext=booktext.lower()
    book_chr={}
    d_char='a'
    d_charNum = ord(d_char)
    for i in range(0,26):
        book_chr[d_char]=0
        d_charNum+=1
        d_char = chr(d_charNum)
    if booktext == "":
        print("ERROR: blank text")
        return 0
    else:
        for b_chr in booktext:
            if b_chr in book_chr:
                book_chr[b_chr] +=1
            else:
                book_chr[b_chr]=1
                continue
        return book_chr
    
def sort_data(book_dict):
    if book_dict=={}:
        print("ERROR: blank dictionary")
        return 0
    else:
        sorted_dict=dict(sorted(book_dict.items(), key=lambda item: item[1], reverse=True))
        return sorted_dict