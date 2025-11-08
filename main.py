from stats import word_count
from stats import char_count
from stats import sort_data
import sys

def get_book_text(filepath):
    contents= ""
    if filepath != "":
        with open(filepath) as f:
            contents = f.read()
    else:
        return "Error filepath blank"
    return contents


def main():
    
    print(sys.argv)
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        m_content ="original content"
        m_wordcount =0
        #UNCOMENT these 3 lines 
        m_content = get_book_text(sys.argv[1])
        m_wordcount = word_count(m_content)
        m_char_count=char_count(m_content)
        m_char_count=sort_data(m_char_count)
   

    
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print ("Found "+str(m_wordcount)+" total words")
        print("--------- Character Count -------")
        for key, value in m_char_count.items():
            if key.isalpha():
                print(f"{key}: {value}")
         
        print("============= END ===============")


   


    deb=0  



main()