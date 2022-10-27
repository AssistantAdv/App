import os
from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
import pywhatkit as kit

def music(query):
    
    try:

        if "songs" in query or "song" in query or "music" in query or "musics" in query:
            
            while True:
                try:
        
                    if "jashne bahara" in query or "jashn e bahara" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\_Jashn E Bahaara - Jodhaa Akbar(PagalWorld.com).mp3")
                        
                    elif "burj khalifa" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 - BurjKhalifa - Laxmii (2020).mp3")
                        
                    elif "ghungru" in query or "ghunghru" in query or "ghungroo" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 - Ghungroo - War (2019).mp3")
                        
                        
                    elif "cheez badi" in query or "chij badi" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 Cheez Badi - Machine - 320Kbps.mp3")
                        
                        
                    elif "chogada" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 Chogada - Loveratri.mp3")
                        
                        
                    elif "dilbar" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 Dilbar - Satyameva Jayate.mp3")
                        
                        
                    elif "hamari adhuri" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 Hamari Adhuri Kahani (Title Song) Arijit Singh 320Kbps.mp3")
                        
                        
                    elif "mohabbat" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 Mohabbat - Fanney Khan.mp3")
                        
                        
                    elif "tere sang yaara" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01 Tere Sang Yaara - Rustom - Atif Aslam - 190Kbps.mp3")
                        
                        
                    elif "aaja nachle" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01. Aaja Nachle.mp3")
                        
                        
                    elif "agar tum miljao" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01. Agar Tum Miljao - Female.mp3")
                        
                        
                    elif "ye tune kya kiya" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\01. Ye Tune Kya Kiya.mp3")
                        
                        
                    elif "bambolle" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\02 - BamBholle - Laxmii (2020).mp3")
                        
                        
                    elif "sweetheart" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\02 - Sweetheart - Kedarnath (2018) (1).mp3")
                        
                        
                    elif "akh lad jave" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\02 Akh Lad Jave - Loveratri.mp3")
                        

                    elif "raataan" in query:
                        speak("")
                        
                    elif "dekhta dekhta" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\02 Dekhte Dekhte - Batti Gul Meter Chalu.mp3")
                        
                        
                    elif "del diyan gallan" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\02 Dil Diyan Gallan - Tiger Zinda Hai (Atif) 320Kbps.mp3")
                        
                        
                    elif "paniyon sa" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\02 Paniyon Sa - Satyameva Jayate.mp3")
                        
                        
                    elif "photocopy" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\03 Photocopy- Jai Ho [PagalWorld.com].mp3")
                        
                        
                    elif "jiya nahi" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Raataan Lambiyan - Shershaah.mp3")
                        

                    elif "tera hua" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\03 Tera Hua - Loveratri.mp3")
                        

                    elif "choti si aasha" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\03. Choti Si Aasha.mp3")
                        

                    elif "hum mar jayenge" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\04 Hum Mar Jayenge - Aashiqui 2 (Arijit Singh) 320Kbps.mp3")
                        

                    elif "rangtari" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\04 Rangtaari - Yo Yo Honey Singh.mp3")
                        

                    elif "dholida" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\05 Dholida - Loveratri.mp3")
                        

                    elif "channa mereya" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\07 Channa Mereya - Arijit Singh 320Kbps.mp3")
                        

                    elif "ghagra" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\07 Ghagra (Yeh Jawaani Hai Deewani).mp3")
                        

                    elif "nagada song dol" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\07 Nagada Sang Dol.mp3")
                        

                    elif "tu jo mila" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\07 Tu Jo Mila (Bajrangi Bhaijaan) KK 190Kbps.mp3")
                        

                    elif "socha hai" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\08 Socha Hai (Love Version) Baadshaho.mp3")
                        

                    elif "baarish" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\12 Baarish - Atif Aslam (Half Girlfriend) 190Kbps.mp3")
                        

                    elif "aaa tera happy birthday" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Aaa Tera Happy Birthday - ABCD  2.mp3")
                        

                    elif "aankh maery" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Aankh Marey - Simmba.mp3")
                        

                    elif "aankh uthi mohabbat ne angrai li" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Aankh Uthi Mohabbat Ne Angrai Li (DjWorldTau.In).mp3")
                        

                    elif "ankhiyon se goli mare" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Ankhiyon Se Goli Mare Returns.mp3")
                        

                    elif "tera hone laga hoon" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\APKGK 2009 - Tera Hone Laga Hoon.mp3")
                        

                    elif "aye khuda tu bol de" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Aye Khuda Tu Bol De(PagalWorld.com.se).mp3")
                        

                    elif "baarish ban jaana" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Baarish Ban Jaana - Payal Dev 320 KbpsBad Boy - Saaho Hindi.mp3")
                        

                    elif "bewafa tera massom chahra" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Bewafa Tera Masoom Chehra - Jubin Nautiyal.mp3")
                        

                    elif "bezubaan kab se" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Bezubaan Kab Se - Street Dancer 3D.mp3")
                        

                    elif "chale aana" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Chale Aana - De De Pyaar De.mp3")
                        

                    elif "chandigarh mein" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Chandigarh Mein - Good Newwz.mp3")
                        

                    elif "chhote chhote peg" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Chhote Chhote Peg - Sonu Ke Titu Ki Sweety.mp3")
                        

                    elif "choodiyan" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Choodiyan - Tanishk Bagchi.mp3")
                        

                    elif "chudi jo khankee" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Chudi Jo Khankee - Bole Jo Koyal Bago Me (1).mp3")
                        

                    elif "coca cola" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Coca Cola - Luka Chuppi.mp3")
                        

                    elif "dhagala lagali" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dhagala Lagali - Dream Girl 128 Kbps.mp3")
                        

                    elif "dheeme dheeme" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dheeme Dheeme - Pati Patni Aur Woh.mp3")
                        

                    elif "dil chori" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dil Chori - Sonu Ke Titu Ki Sweety.mp3")
                        

                    elif "dil ibaadat" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dil Ibaadat - Tum Mile 320Kbps.mp3")
                        

                    elif "dil ka telephone" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dil Ka Telephone - Dream Girl 128 Kbps.mp3")
                        

                    elif "dil ke paas" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dil Ke Paas (Wajah Tum Ho) Arijit Singh 320Kbps.mp3")
                        

                    elif "dil mera blast" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dil Mera Blast - Darshan Raval 320 Kbps.mp3")
                        

                    elif "dil ne yeh kaha hai dil se" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dil Ne Yeh Kaha Hai Dil Se - (amlijatt.in).mp3")
                        

                    elif "dil royi jaye" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dil Royi Jaye - De De Pyaar De.mp3")
                        

                    elif "dilbara" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dilbara - B Praak Version.mp3")
                        

                    elif "dua karo" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Dua Karo - Street Dancer 3D.mp3")
                        

                    elif "duaa" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Duaa - Arijit Singh - 320Kbps.mp3")
                        

                    elif "duniyaa" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Duniyaa - Luka Chuppi.mp3")
                        

                    elif "ek passe tu babbu" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Ek Passe Tu Babbu - Sakhiyaan.mp3")
                        

                    elif "ek toh kum zindagani" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Ek Toh Kum Zindagani - Marjaavaan.mp3")
                        

                    elif "enni soni" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Enni Soni - Saaho.mp3")
                        

                    elif "first class" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\First Class - Kalank.mp3")
                        

                    elif "gali gali" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Gali Gali - KGF.mp3")
                        

                    elif "garmi" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Garmi - Street Dancer 3D.mp3")
                        

                    elif "genda phool" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Genda Phool - Badshah.mp3")
                        

                    elif "dil meri na sune" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Genius 2018 - Dil Meri Na Sune.mp3")
                        

                    elif "pyar le pyar de" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Genius 2018 - Pyar Le Pyar De.mp3")
                        

                    elif "tera fitoor" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Genius 2018 - Tera Fitoor.mp3")
                        

                    elif "tujhse kahan juda hoon main" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Genius 2018 - Tujhse Kahan Juda Hoon Main.mp3")
                        

                    elif "haiya ho" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Haiya Ho - Marjaavaan.mp3")
                        

                    elif "happy birthday to you ji" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Happy Birthday To You Ji .mp3")
                        

                    elif "hauli hauli" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Hauli Hauli - De De Pyaar De.mp3")
                        

                    elif "high rated gabru" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\High Rated Gabru - Guru Randhawa 320Kbps.mp3")
                        

                    elif "hum teri mohabbat mein" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Hum Teri Mohabbat Mein_192(PaglaSongs).mp3")
                        

                    elif "humnava mere" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Humnava Mere - Jubin Nautiyal.mp3")
                        

                    elif "husnn hai suhaana" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Husnn Hai Suhaana New - Coolie No 1.mp3")
                        

                    elif "ik mulaqaat" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Ik Mulaqaat - Dream Girl 128 Kbps.mp3")
                        

                    elif "illegal weapon 2" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Illegal Weapon 2 - Street Dancer 3D.mp3")
                        

                    elif "ishare teri karti nigah" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Ishare Tere Karti Nigah - Sumit Goswami 320Kbps(DJPubg.Com).mp3")
                        

                    elif "jab koi baat" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Jab Koi Baat - Atif Aslam n Shirley Setia 190Kbps.mp3")
                        

                    elif "jab teri yaad aayegi" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Jab Teri Yaad Aayegi - I Shoj Kytrak.mp3")
                        

                    elif "jai jai shivshankar" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Jai Jai Shivshankar - War.mp3")
                        

                    elif "kamariya" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Kamariya - Mitron 320 Kbps.mp3")
                        

                    elif "kamar teri left right hale" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\kamar-teri-left-right-hale-(mobVD.com).mp3")
                        

                    elif "kinna sona" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Kinna Sona - Marjaavaan.mp3")
                        

                    elif "lagdi lahore di" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Lagdi Lahore Di - Street Dancer 3D.mp3")
                        

                    elif "lehanga" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Lehanga - Jass Manak.mp3")
                        

                    elif "main balak to mata" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Main Balak Tu Mata_192(PagalWorld).mp3")
                        

                    elif "main jahhan rahoon" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Main Jahaan Rahoon (Namastey London) -320Kbps [Rahat Fateh].mp3")
                        

                    elif "maine tumko chaha tumse" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Maine+Tumko+Chaha+Tumse+Pyar+Kiya+मैंने+तुमको+चाहा+तुमसे+प्यार+किया.mp3")
                        

                    elif "maiya teri jai jaikaar" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Maiya Teri Jai Jaikaar - Arijit Singh 320Kbps.mp3")
                        

                    elif "mein chali mein chali" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Mein Chali Mein Chali 320Kbps(DJPubg.Com).mp3")
                        

                    elif "mera wala dance" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Mera Wala Dance - Simmba.mp3")
                        

                    elif "meri aashiqui" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Meri Aashiqui - Jubin Nautiyal.mp3")
                        

                    elif "mohabbat ka gam hai" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Mohabbat Ka Gam Hai Mile Jitna Kam Hai 320Kbps(DJPubg.Com).mp3")
                        

                    elif "mukhada vakh ke" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Mukhda Vekh Ke - De De Pyaar De.mp3")
                        

                    elif "muqabla" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Muqabla - Street Dancer 3D.mp3")
                        

                    elif "naah goriye" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Naah Goriye - Bala.mp3")
                        

                    elif "naina" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Naina - Dangal (Arijit Singh) 190Kbps.mp3")
                        

                    elif "namo namo" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Namo Namo - Kedarnath.mp3")
                        

                    elif "o saki saki" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\O Saki Saki - Batla House 320 Kbps.mp3")
                        

                    elif "odhani" in query or "odani" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Odhani - Made in China.mp3")
                        

                    elif "pachtaoge" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Pachtaoge - Arijit Singh 128 Kbps.mp3")
                        

                    elif "paniyon sa " in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Paniyon Sa (Satyameva Jayate) 320 Kbps.mp3")
                        

                    elif "phir bhi tumko chaahinga" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Phir+Bhi+Tumko+Chaahunga+8D+Audio+Arijit+Singh.mp3")
                        

                    elif "photo" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Photo - Luka Chuppi.mp3")
                        

                    elif "poster lagwa do" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Poster Lagwa Do - Luka Chuppi.mp3")
                        

                    elif "psycho saiyaan" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Psycho Saiyaan - Saaho - Hindi.mp3")
                        

                    elif "pyar kiya to nibhana" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Pyar Kiya To Nibhana - Ajay Devgan (Original) 190Kbps.mp3")
                        

                    elif "qaafirana" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Qaafirana - Kedarnath.mp3")
                        

                    elif "radha" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Radha (Student Of The Year).mp3")
                        

                    elif "radhe radhe" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Radhe Radhe - Dream Girl 128 Kbps.mp3")
                        

                    elif "relation" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Relation - Nikk.mp3")
                        

                    elif "rula ke gaya ishq" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Rula Ke Gaya Ishq - Stebin Ben.mp3")
                        

                    elif "saal bhar mein sabse pyara " in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Saal Bhar Mein Sabse Pyara Happy Birthday943_Cut audio_Jun 17.mp3")
                        

                    elif "sab tera" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Sab Tera - Baaghi (Shraddha Kapoor) 320Kbps.mp3")
                        

                    elif "sanedo" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Sanedo - Made in China.mp3")
                        

                    elif "sauda khara khara" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Sauda Khara Khara - Good Newwz.mp3")
                        

                    elif "sheher ki ladki" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Sheher Ki Ladki - Khandaani Shafakhana.mp3")
                        

                    elif "bom diggy diggy" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\SKTKS - Bom Diggy Diggy.mp3")
                        

                    elif "slow motion" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Slow Motion - Bharat236_Cut audio_Jul 25.mp3")
                        

                    elif "so gaya yeh jahan" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\So Gaya Yeh Jahan - Bypass Road.mp3")
                        

                    elif "sooraj dooba hain" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Sooraj Dooba Hain - Arijit Singh - 320Kbps.mp3")
                        

                    elif "taaron ke sheher" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Taaron Ke Shehar - Neha Kakkar.mp3")
                        

                    elif "tera baap aaya" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tera Baap Aaya - Commando 3.mp3")
                        

                    elif "tera ghata" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tera Ghata - Gajendra Verma.mp3")
                        

                    elif "teri aankhon mein" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Teri Aankhon Mein - Darshan Raval (1).mp3")
                        

                    elif "teri mitti" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Teri Mitti - Kesari.mp3")
                        

                    elif "thodi jagah" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Thodi Jagah - Marjaavaan.mp3")
                        

                    elif "tu hi yaar mera" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tu Hi Yaar Mera - Pati Patni Aur Woh955_Cut audio_Jun 07.mp3")
                        

                    elif "tu jaane na" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tu Jaane Na - Ajab Prem Ki Ghazab Kahani 320 Kbps.mp3")
                        

                    elif "tu laung main elachi" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tu Laung Main Elaachi - Luka Chuppi.mp3")
                        

                    elif "tum hi aana" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tum Hi Aana - Marjaavaan.mp3")
                        

                    elif "tum mile dil khile" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tum Mile Dil Khile (New Version) - Arijit Singh 320Kbps(DJPubg.Com).mp3")
                        

                    elif "tum par hum hai atke" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Tum Par Hum Hai Atke - Pagalpanti.mp3")
                        

                    elif "vaddi sharaban" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Vaddi Sharaban - De De Pyaar De.mp3")
                        

                    elif "valam" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Valam - Made in China.mp3")
                        

                    elif "va mahi" in query:
                        speak("Enjoy this song")
                        os.startfile("E:\\music\\Ve Maahi - Kesari.mp3")
                        
                        
                    elif "none" in query:
                        speak("please sir tell me name of music")
                    
                    elif "exit" in query or "stop" in query:
                        speak("Exiting...")
                        break

                    else:
                        speak("Unavailable to this song")
                        break
                    
                except Exception:
                    speak("No song available in your system")

        elif "video" in query or "video songs" in query or "videos" in query or "songs on youtube" in query or "videos on youtube" in query:
        
            if "video" in query:
                speak("Tell me name of the video")

            elif "video song" in query:
                speak("Tell me name of the video songs")

            elif "videos" in query:
                speak("Tell me name of the videos")

            elif "song on youtube" in query:
                speak("Tell me name of the songs play on youtube")

            elif "video on youtube" in query:
                speak("Tell me name of the videos play on youtube")

            while True:
                vi = takecom()
                if "none" in vi:
                    speak("Please tell me which video or song play")
                elif "exit" in vi or "stop" in vi:
                    speak("Exiting...")
                    break
                else:
                    kit.playonyt(f"playing {vi}")
                    speak("Exiting...")
                    

    except Exception:
        speak("Error")

