from pythainlp import sent_tokenize, word_tokenize

texts = [
    ("พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว พุทธศักราช ๒๔๗๕ "
     "เป็นรัฐธรรมนูญฉบับชั่วคราว ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม "
     "ประกาศใช้เมื่อวันที่ 27 มิถุนายน พ.ศ. 2475 "
     "โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่ 24 มิถุนายน พ.ศ. 2475 โดยคณะราษฎร"),

    """ยะลาอ่วม ฝนตกหนัก ดินสไลด์ทับเส้นทาง น้ำคลองกัดเซาะถนนภายในหมู่บ้านขาด น้ำหลากท่วมบ้านเรือนประชาชนหลายหลัง

เมื่อเวลา18.40 น. วันที่ 11 ต.ค.2567 ผู้สื่อข่าวรายงาน ในพื้นที่ ต.อัยเยอร์เวง อ.เบตง จ.ยะลา เกิดฝนตกหนัก ทำให้ดินสไลด์ทับเส้นทาง น้ำคลองกัดเซาะถนนภายในหมู่บ้านขาด น้ำหลากท่วมบ้านเรือนประชาชนหลายหลัง นอกจากนั้นยังเกิดดินสไลด์ปิดทับเส้นทางสาย 410 เบตง-ยะลา ช่วงกม.39."""
]

sentence_engines = [ "whitespace+newline", "whitespace", "newline", "thaisum", "wtp", "wtp-tiny" ]
# default engine ("") not available as it uses pycrfsuite, which is an extra dependency.  Skipping
# "tltk" tltk is extra dependency, has build deps so might cause trouble -- on mac, ERROR: Command errored out with exit status 1:

word_engines = [ "newmm", "newmm-safe", "longest" ]

# "attacut" word engine not available due to "ERROR: Could not find a version that satisfies the requirement torch>=1.2.0 (from attacut) (from versions: none)"
# "tltk" tltk is extra dependency, has build deps so might cause trouble -- on mac, ERROR: Command errored out with exit status 1:

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
