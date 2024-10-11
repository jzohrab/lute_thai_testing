# -*- coding: utf-8 -*-
from pythainlp import sent_tokenize, word_tokenize
import sys

texts = [
    ("พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว พุทธศักราช ๒๔๗๕ "
     "เป็นรัฐธรรมนูญฉบับชั่วคราว ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม "
     "ประกาศใช้เมื่อวันที่ 27 มิถุนายน พ.ศ. 2475 "
     "โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่ 24 มิถุนายน พ.ศ. 2475 โดยคณะราษฎร"),

    """ยะลาอ่วม ฝนตกหนัก ดินสไลด์ทับเส้นทาง น้ำคลองกัดเซาะถนนภายในหมู่บ้านขาด น้ำหลากท่วมบ้านเรือนประชาชนหลายหลัง

เมื่อเวลา18.40 น. วันที่ 11 ต.ค.2567 ผู้สื่อข่าวรายงาน ในพื้นที่ ต.อัยเยอร์เวง อ.เบตง จ.ยะลา เกิดฝนตกหนัก ทำให้ดินสไลด์ทับเส้นทาง น้ำคลองกัดเซาะถนนภายในหมู่บ้านขาด น้ำหลากท่วมบ้านเรือนประชาชนหลายหลัง นอกจากนั้นยังเกิดดินสไลด์ปิดทับเส้นทางสาย 410 เบตง-ยะลา ช่วงกม.39.""",
]

extra_news = """เมืองคอนฝนตกหนัก น้ำป่าไหลหลากลงสู่คลองวังลุง ซัด 3 นักท่องเที่ยวชาวภูเก็ตจมหาย พบเสียชีวิต 2 ศพ ช่วยรอด 1 ราย

วันที่ 11 ตุลาคม 2567 มีรายงานว่า จากเหตุการณ์ฝนตกหนักบนเทือกเขาหลวงนครศรีธรรมราช เมื่อเวลา 16.30 น. ที่ผ่านมา ทำให้เกิดน้ำป่าไหลหลากลงสู่คลองวังลุง ม.6 ต.ทอนหงส์ อ.พรหมคีรี จ.นครศรีธรรมราช ส่งผลให้นักท่องเที่ยวจาก จ.ภูเก็ต ที่ได้ลงเล่นน้ำในลำคลองดังกล่าวไม่ทันระวังตัว ถูกน้ำป่าที่ไหลเชี่ยวกรากพัดร่าง 3 คน ไหลลอยไปกับกระแสน้ำไม่มีใครสามารถช่วยได้ทัน

หลังจากเกิดเหตุแล้ว เพื่อนนักท่องเที่ยวและพนักงานของแคมป์ได้แจ้งให้เจ้าหน้าที่หน่วยกู้ภัยต่างๆ ในพื้นที่ รวมทั้งเจ้าหน้าที่ฝ่ายปกครองในพื้นที่นำโดยนายอำเภอพรหมคีรี และปลัดอำเภอพรหมคีรี และกำนัน ผู้ใหญ่บ้านในพื้นที่ได้ระดมกำลังช่วยเหลือนักท่องเที่ยวรอดชีวิตมาได้ 1 ราย ชื่อนางอรวรรณ อายุ 42 ปี ชาว จ.ภูเก็ต มีอาการสำลักน้ำถูกนำส่ง รพ.พรหมคีรี อาการปลอดภัยแล้ว"""

texts.append(extra_news)

sentence_engines = [ "thaisum", "whitespace" ]
# default engine ("") not available as it uses pycrfsuite, which is an extra dependency.  Skipping
# "tltk" tltk is extra dependency, has build deps so might cause trouble -- on mac, ERROR: Command errored out with exit status 1:
# "newline" not found - fine, I'll split that anyway
# "whitespace+newline" - Lute will split by paragraphs (newlines), so don't use that for sentence tokenizing.
# "wtp" is extra install - from wtpsplit import WtP

word_engines = [ "newmm", "newmm-safe", "longest" ]

# "attacut" word engine not available due to "ERROR: Could not find a version that satisfies the requirement torch>=1.2.0 (from attacut) (from versions: none)"
# "tltk" tltk is extra dependency, has build deps so might cause trouble -- on mac, ERROR: Command errored out with exit status 1:

# Finding sentences.
tnum = 0
for text in texts:
    tnum += 1
    print("=" * 50)
    print(f"Sample text #{tnum}:")
    print("-" * 50)
    print(text)
    print("-" * 50)
    print()

    for se in sentence_engines:
        print()
        print("Sentence engine = " + se)
        sentences = sent_tokenize(text, engine=se)
        senum = 0
        for s in sentences:
            senum += 1
            print()
            print(f"{senum}: {s}")

# Tokenizing sentences
for text in texts:
    for se in sentence_engines:
        sentences = sent_tokenize(text, engine=se)
        for s in sentences:
            print()
            print(f"Tokens for sentence \"{s}\":")
            results = {}
            for we in word_engines:
                tokens = word_tokenize(s, engine=we)
                jt = ", ".join(tokens)
                if jt in results:
                    results[jt].append(we)
                else:
                    results[jt] = [we]
            for jt, engines in results.items():
                if len(engines) == len(word_engines):
                    print(jt)
                else:
                    print(f"{jt} (engines: {', '.join(engines)})")


sys.exit(0)

for text in texts:
    print("=" * 50)
    print(text)
    print()

    for se in sentence_engines:
        print("Sentence engine = " + se)
        sentences = sent_tokenize(text, engine=se)
        senum = 0
        for s in sentences:
            senum += 1
            print(f"{senum}: {s}")
            for we in word_engines:
                print("Word engine = " + we)
                tokens = word_tokenize(s, engine=we)
                print(tokens)
