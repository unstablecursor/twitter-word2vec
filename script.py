import word2vec
model = word2vec.load('ress.bin')
print model.vocab[5]
metrics = model.cosine('#Evet')
print model.generate_response('#Evet', metrics).tolist()
