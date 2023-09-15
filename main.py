meme_dict = {
    "gabut" : "tidak ada kegiatan",
    "gaje" : "tidak jelas",
    "santuy" : "santai",
    "Healing" : "liburan",
    "otw" : "lagi di jalan",
    "jamber" : "jam berapa?",
    "kuy" : "ayo",
    "tbl" : "takut banget lho",
    "ygy" : "ya guys ya",
    "mantul" : "mantap betul",
    "overthinking" : "banyak pikiran",
    "gercep" : "gerak cepet",
    "mager" : "males gerak",
    "crush" : "gebetan",
    "fomo" : "takut ketinggalan tren",
    "cepu" : "tidak bisa menjaga rahasia",
    "gemoy" : "gemuk lucu",
    "glow up" : "lebih baik/lebih menawan",
    "bestie" : "best friend atau teman dekat",
    "circle" : "lingkaran pertemanan",
}
    
for i in range(5):
    word = input("Ketik kata yang tidak kamu mengerti: ")
    if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata  itu ditemukan?
        print (meme_dict[word])
    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print("kata gaul tersebut tidak terdaftar di kamus")
