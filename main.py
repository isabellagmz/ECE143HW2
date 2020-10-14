import powers_of_3 as pw
import write_columns as wc
import nonoverlapping_sequences as nos

class Homework2:
    def __init__(self):
        pass

if __name__ == '__main__':
    #data = [5, 4, 6, 1, 9, 0, 3, 9, 2, 7, 10, 8, 4, 7, 1, 2, 7, 6, 5, 2, 8, 2, 0, 1, 1, 1, 2, 10, 6, 2]

    words = ["the", "of", "and", "to", "a","in","for","is","on", "that","by","this", "with","i","you",
             "it","not","or","be","are","from","at","as","your","all","have","new","more","an","was",
             "we","will","home","can","us","about",'if',"page","my","has",'search',"free","but","our",
             "one","other","do","no","information"]
    fname = "fname"

    my_Homework2 = Homework2()
    nos.write_chunks_of_five(words,fname)
    #wc.write_columns(data, fname)
    #pw.get_power_of3(40)
