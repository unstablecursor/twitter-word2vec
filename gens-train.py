
import gensim
input_file = input("Input file:")
output_file = input("Output file (.w2v):")
sentences = gensim.models.word2vec.LineSentence(input_file, max_sentence_length=10000)
model = gensim.models.Word2Vec()
model.build_vocab(sentences)
model.train(sentences)
model.save(output_file)
