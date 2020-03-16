from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()

mode = tokenizer.Tokenizer.SplitMode.A

txt = "医薬品安全管理責任者"
mode = tokenizer.Tokenizer.SplitMode.A
print([m.surface() for m in tokenizer_obj.tokenize(txt, mode)])
mode = tokenizer.Tokenizer.SplitMode.B
print([m.surface() for m in tokenizer_obj.tokenize(txt, mode)])
mode = tokenizer.Tokenizer.SplitMode.C
print([m.surface() for m in tokenizer_obj.tokenize(txt, mode)])