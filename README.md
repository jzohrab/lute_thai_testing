Testing out `pythainlp` ([ref](https://pythainlp.org/tutorials/notebooks/pythainlp_get_started.html)) for [Lute](https://luteorg.github.io/lute-manual/intro.html), see what are the best sentence and word tokenizers.

`pythainlp` has different "engines" to split sentences (`[ "thaisum", "whitespace" ]`) and words (`[ "newmm", "newmm-safe", "longest" ]`), so `main.py` shows examples for each of these with 3 text samples.

Results are at [sample_output.txt](./sample_output.txt) -- see below for notes.

# interpreting the results

## sentence splitting

e.g. with sample text 1, the thaisum engine splits it into 4 sentences, but the whitespace engine splits it into many.

```
Sample text #1:
--------------------------------------------------
พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว พุทธศักราช ๒๔๗๕ เป็นรัฐธรรมนูญฉบับชั่วคราว ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม ประกาศใช้เมื่อวันที่ 27 มิถุนายน พ.ศ. 2475 โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่ 24 มิถุนายน พ.ศ. 2475 โดยคณะราษฎร
--------------------------------------------------


Sentence engine = thaisum
1: พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว พุทธศักราช ๒๔๗๕ เป็นรัฐธรรมนูญฉบับชั่วคราว
2: ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม ประกาศใช้เมื่อวันที่ 27 มิถุนายน พ.ศ. 2475
3: โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่ 24 มิถุนายน พ.ศ. 2475
4: โดยคณะราษฎร

Sentence engine = whitespace
1: พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว
2: พุทธศักราช
3: ๒๔๗๕
4: เป็นรัฐธรรมนูญฉบับชั่วคราว
5: ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม
6: ประกาศใช้เมื่อวันที่
7: 27
8: มิถุนายน
9: พ.ศ.
10: 2475
11: โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่
12: 24
13: มิถุนายน
14: พ.ศ.
15: 2475
16: โดยคณะราษฎร
```

## tokenizing sentences

This section takes the sentences for each of the sentence splitting results, and then tokenizes them using different tokenizing engines.

As shown below, all engines returned the same tokens for the first two sentences.  For the third, newmm and newmm-safe returned the same tokens, but the "longest" engine returned something slightly different.

```
"พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว พุทธศักราช ๒๔๗๕ เป็นรัฐธรรมนูญฉบับชั่วคราว":
  พระราชบัญญัติ, ธรรมนูญ, การปกครอง, แผ่นดิน, สยาม, ชั่วคราว,  , พุทธศักราช,  , ๒๔๗๕,  , เป็น, รัฐธรรมนูญ, ฉบับ, ชั่วคราว

"ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม ประกาศใช้เมื่อวันที่ 27 มิถุนายน พ.ศ. 2475":
  ซึ่ง, ถือว่า, เป็น, รัฐธรรมนูญ, ฉบับ, แรก, แห่ง, ราชอาณาจักร, สยาม,  , ประกาศใช้, เมื่อ, วันที่,  , 27,  , มิถุนายน,  , พ.ศ.,  , 2475

"โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่ 24 มิถุนายน พ.ศ. 2475":
  โดย, เป็น, ผลพวง, หลัง, การปฏิวัติ, เมื่อ, วันที่,  , 24,  , มิถุนายน,  , พ.ศ.,  , 2475 (newmm, newmm-safe)
  โดย, เป็นผล, พวง, หลัง, การปฏิวัติ, เมื่อ, วันที่,  , 24,  , มิถุนายน,  , พ.ศ.,  , 2475 (longest)
```

newmm and newmm-safe almost always returned the same results.

# dev usage

create a venv, install all reqs, then run main.py: `python main.py`
