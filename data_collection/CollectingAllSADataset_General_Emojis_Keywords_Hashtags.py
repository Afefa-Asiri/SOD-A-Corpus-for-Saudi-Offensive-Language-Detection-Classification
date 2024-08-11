# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:36:23 2022

@author: aafef
"""

"""
* In this file, we collect OFFENSIVE tweets from all the 13 regions of Saudi Arabia 
[Riyadh, Makkah, Eastern, Asir, Jizan, Madina, Al-Qassim, Tabuk, Hail, Najran, Al-Jawf, Al-Baha, Northern Borders] 
- According to their Main Cities: [ Riyadh, Jeddah, Dammam, Abha, Jizan, Buraidah, Tabuk, Najran, Aljawf, Al-Baha, ArAr]
- within 300K to 50K around the main city, depends on the location results. 
    . we adjusted the around kilos to avoid collecting unwanted Location. 
- The tweets will be collected in the last 4 years [ 2019-2022]. 
- We separate a yearly time interval, to ensure that the collection covered all the period not only the first tweets in the first-time interval in the searching process.    


* Data % in the collected data related to the % of the population in each region:
	Riyadh: 23%               | around 250k  R   Riyadh
	Makkah: 22%               | around 300k  J   Jeddah
	Eastern: 15%              | around 200k  D   Dammam
	Asir: 9%                  | around 150k  A   Abha
	Jizan: 6%                 | around 150k  Jz  Jizan
	Medina: 7%                | around 100k  M   24.470901, 39.612236  #We use the coordination as the name of the city was showed inaccurate results
	Al-Qassim: 5%             | around 100k  B   Buraidah
	Tabuk: 3%                 | around 100k  T   Tabuk
	Hail: 3%                  | around 100k  H   Hail
	Najran: 2%                | around 50k   N   Najran
	Al-Jawf: 2%               | around 50k   Jw  29.5,39.52236         #We use the coordination as the name of the city was showed inaccurate results
	Al-Baha: 2%               | around 50k  Bah  20.0125, 41.465278    #We use the coordination as the name of the city was showed inaccurate results
	Northern Borders: 1%      | around 50k  ArAr  Arar

***********************[ General ]************************************
Firstly, we collecting general tweets related to each SA region, the following list represents the collecting (City, How many KM around the City, No of Tweets)
GeneralList=[('Riyadh','250k','50000'), ('Jeddah','300k','50000'), ('Dammam','200k','30000'), ('Abha','150k','10000'), ('Jizan','150k','10000'), ('24.470901, 39.612236','100k','10000'), ('Buraidah','100k','10000'), ('Tabuk','100k','10000'), ('Hail','100k','10000'), ('Najran','50k','10000'), ('29.5,39.52236','50k','10000'), ('20.0125, 41.465278','50k','10000'), ('Arar','50k','10000')]

***********************[ Emojis ]************************************
GeneralListEmojis=[('Riyadh','250k','1000'), ('Jeddah','300k','1000'), ('Dammam','200k','1000'), ('Abha','150k','500'), ('Jizan','150k','500'), ('24.470901, 39.612236','100k','500'), ('Buraidah','100k','500'), ('Tabuk','100k','500'), ('Hail','100k','500'), ('Najran','50k','500'), ('29.5,39.52236','50k','500'), ('20.0125, 41.465278','50k','500'), ('Arar','50k','500')]
ٍSecondly, with the specification as on the general search, with adjusment on #No of Tweets, we collected Tweets based on Emojis search:
- The Collection process will be based on Offensive Emojis Search suggested by Hamdy Mubark et. al.
in their paper: Emojis as Anchors to Detect Arabic Offensive Language and Hate Speech
EmojisList= ['💦', '🐖', '🐷', '🐽', '👞', '🐕', '🐶', '💩', '🐄', '🐮', '🐑', '🐏', '👎', '😡', '🤬', '👺', '👿', '😠']

***********************[ Keywords ]***********************************
GeneralListKeywords=[('Riyadh','250k','1000'), ('Jeddah','300k','1000'), ('Dammam','200k','1000'), ('Abha','150k','500'), ('Jizan','150k','500'), ('24.470901, 39.612236','100k','500'), ('Buraidah','100k','500'), ('Tabuk','100k','500'), ('Hail','100k','500'), ('Najran','50k','500'), ('29.5,39.52236','50k','500'), ('20.0125, 41.465278','50k','500'), ('Arar','50k','500')]
Thirdly, with the specification as on the general search, with adjusment on #No of Tweets, we collected Tweets based on Keywords search, which represents: Offensive, Race, Ideology [Sport, Religion] and Gender:
KeywordsList=['يلعن' , 'قلة أدب' , 'وسخ' , 'وقح' , 'كلب' , 'حمار' , 'خنزير' , 'زبالة' , 'تفو عليك' , 'خسيس' , 'نذل' , 'ياحيوان' , 'نجس' , 'يايمني' , 'يايماني' , 'يامصري' , 'ياهندي' , 'يابنقالي' , 'طاقية' , 'دوري يلو' , 'أهلي' , 'هلال' , 'اتحاد' , 'نصراوي' , 'طحالب' , 'تماسيح' , 'سحالي' , 'نصر' , 'اتحادي' , 'هلالي' ,  'هلال' , 'أهلاوي' , 'شبابي' , 'يابدوي' , 'ياحضري' , 'يابدو' , 'ياحضر' , 'ياقروي' , 'ياخضيري' , 'طرش بحر' , 'بقايا حجاج' , 'أعرابي' , 'حجازي' , 'نجدي' , 'قصيمي' , 'حساوي' , 'زيدي' , 'زيود' , 'يابيض' , 'ذباب الكتروني' , 'ياشيعي' , 'ياسني' , 'ياداعشي' , 'ياأخواني' , 'ياوطنجي' , 'ياإرهابي' , 'داعشي' , 'إرهابي' , 'سني' , 'شيعي' , 'إيراني' , 'أخواني' , 'ليبرالي' , 'حرمة' , 'ياحريم' , 'يابنت' , 'البنات' , 'الرجال' , 'رجل' , 'الرياجيل' , 'بنات اليوم' , 'أولاد اليوم' , 'الأولاد']
***********************[ Hashtags ]***********************************
GeneralListHashtags=[('Riyadh','250k','1000'), ('Jeddah','300k','1000'), ('Dammam','200k','1000'), ('Abha','150k','500'), ('Jizan','150k','500'), ('24.470901, 39.612236','100k','500'), ('Buraidah','100k','500'), ('Tabuk','100k','500'), ('Hail','100k','500'), ('Najran','50k','500'), ('29.5,39.52236','50k','500'), ('20.0125, 41.465278','50k','500'), ('Arar','50k','500')]
Finally, with the specification as on the general search, with adjusment on #No of Tweets, we collected Tweets based on #hashtags search, which represents: Offensive, Race, Ideology [Sport, Religion] and Gender:
HashtagsList= ["#الشباب" , "#النصر" , "#الهلال" , "#الأهلي" , "#الاتحاد" , "#الدوري_ألسعودي" , "#التماسيح" , "#الطحالب" , "#النمور" , "#حضر" , "#بدو" , "#نسوية" , "#نسوي" , "#ذكورية" , "#ذكوري" , "#مستقلة" , "#حرة"]
"""
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
from datetime import datetime


#General Variabls 
TimeInterval=['since:2019-01-01 until:2019-12-31', 'since:2020-01-01 until:2020-12-31', 'since:2021-01-01 until:2021-12-31', 'since:2022-01-01 until:2022-12-14']


#******************[ Start : General Collection ]************************
now = datetime.now()
print("ٍGENERAL: Starting Time =", now.strftime("%H:%M:%S"))

GeneralList=[('Riyadh','250','50000'), ('Jeddah','300','50000'), ('Dammam','200','30000'), ('Abha','150','10000'), ('Jizan','150','10000'), ('24.470901, 39.612236','100','10000'), ('Buraidah','100','10000'), ('Tabuk','100','10000'), ('Hail','100','10000'), ('Najran','50','10000'), ('29.5,39.52236','50','10000'), ('20.0125, 41.465278','50','10000'), ('Arar','50','10000')]
GeneralTweets=pd.DataFrame()

for c in GeneralList:
    City=c[0]
    km=c[1]
    tw=c[2]
    for Ti in TimeInterval:
        GeneralTweets_i= pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"" near:{} within:{}km {}'.format(City,km,Ti)).get_items(), int('{}'.format(tw))))
        if not GeneralTweets_i.empty:
            GeneralTweets_i['user_location'] = GeneralTweets_i['user'].apply(lambda x: x['location'])
            GeneralTweets_i['City'] = '{}'.format(City) #to chunck the df based on the city column
            GeneralTweets_i['Search'] = 'ByLocation' #To know the type of searching for this tweet, when concatenate all the files
            GeneralTweets=pd.concat([GeneralTweets,GeneralTweets_i]) 
        
#All the Saudi Reigonal Tweets | Searching by General 
GeneralTweets.to_csv('GeneralTweets.csv')

now = datetime.now()
print("GENERAL: Ending Time =", now.strftime("%H:%M:%S"))

#******************[  End  : General Collection ]************************

#........................................................................

#******************[ Start :     By Emojis      ]************************
now = datetime.now()
print("EMOJIS: Starting Time =", now.strftime("%H:%M:%S"))

GeneralListEmojis=[('Riyadh','250','2000'), ('Jeddah','300','2000'), ('Dammam','200','1000'), ('Abha','150','500'), ('Jizan','150','500'), ('24.470901, 39.612236','100','500'), ('Buraidah','100','500'), ('Tabuk','100','500'), ('Hail','100','500'), ('Najran','50','500'), ('29.5,39.52236','50','500'), ('20.0125, 41.465278','50','500'), ('Arar','50','500')]
EmojisList= ['💦', '🐖', '🐷', '🐽', '👞', '🐕', '🐶', '💩', '🐄', '🐮', '🐑', '🐏', '👎', '😡', '🤬', '👺', '👿', '😠']

EmojisTweets=pd.DataFrame()
NoEmojiTweetList=["Nothing", "Test"]

for c in GeneralListEmojis:
    City=c[0]
    km=c[1]
    tw=c[2]
    for Ti in TimeInterval:
        for E in EmojisList:
            EmojisTweets_i= pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"{}" near:"{}" within:{}km {}'.format(E,City,km,Ti)).get_items(), int('{}'.format(tw))))
        if not EmojisTweets_i.empty:
            EmojisTweets_i['user_location'] = EmojisTweets_i['user'].apply(lambda x: x['location'])
            EmojisTweets_i['City'] = '{}'.format(City) #to chunck the df based on the city column
            EmojisTweets_i['Search'] = 'ByEmojis' #To know the type of searching for this tweet, when concatenate all the files
            EmojisTweets=pd.concat([EmojisTweets,EmojisTweets_i])  
        else:
            NoEmojiTweetList.append("{} Does not have Tweets with {} emoji in this Time Interval {}".format(City,E,Ti))
#All the Saudi Reigonal Tweets | Searching by Emojis 
EmojisTweets.to_csv('EmojisTweets.csv')
#File for each city and the missing emoji:
NoEmojiTweetDF=pd.DataFrame(NoEmojiTweetList) #Check If we need to change it inot dataframe
NoEmojiTweetDF.to_csv("MissingEmojisInTweets.csv")

now = datetime.now()
print("EMOJIS: Ending Time =", now.strftime("%H:%M:%S"))

#******************[  End  :     By Emojis      ]************************

#........................................................................

#******************[ Start :     By Keywords    ]************************

now = datetime.now()
print("KEYWORDS: Starting Time =", now.strftime("%H:%M:%S"))

GeneralListKeywords=[('Riyadh','250','1000'), ('Jeddah','300','1000'), ('Dammam','200','1000'), ('Abha','150','500'), ('Jizan','150','500'), ('24.470901, 39.612236','100','500'), ('Buraidah','100','500'), ('Tabuk','100','500'), ('Hail','100','500'), ('Najran','50','500'), ('29.5,39.52236','50','500'), ('20.0125, 41.465278','50','500'), ('Arar','50','500')]
KeywordsList=['يلعن' , 'قلة أدب' , 'وسخ' , 'وقح' , 'كلب' , 'حمار' , 'خنزير' , 'زبالة' , 'تفو عليك' , 'خسيس' , 'نذل' , 'ياحيوان' , 'نجس' , 'يايمني' , 'يايماني' , 'يامصري' , 'ياهندي' , 'يابنقالي' , 'طاقية' , 'دوري يلو' , 'أهلي' , 'هلال' , 'اتحاد' , 'نصراوي' , 'طحالب' , 'تماسيح' , 'سحالي' , 'نصر' , 'اتحادي' , 'هلالي' ,  'هلال' , 'أهلاوي' , 'شبابي' , 'يابدوي' , 'ياحضري' , 'يابدو' , 'ياحضر' , 'ياقروي' , 'ياخضيري' , 'طرش بحر' , 'بقايا حجاج' , 'أعرابي' , 'حجازي' , 'نجدي' , 'قصيمي' , 'حساوي' , 'زيدي' , 'زيود' , 'يابيض' , 'ذباب الكتروني' , 'ياشيعي' , 'ياسني' , 'ياداعشي' , 'ياأخواني' , 'ياوطنجي' , 'ياإرهابي' , 'داعشي' , 'إرهابي' , 'سني' , 'شيعي' , 'إيراني' , 'أخواني' , 'ليبرالي' , 'حرمة' , 'ياحريم' , 'يابنت' , 'البنات' , 'الرجال' , 'رجل' , 'الرياجيل' , 'بنات اليوم' , 'أولاد اليوم' , 'الأولاد']
KeywordsTweets=pd.DataFrame()
NoKeywordTweetList=["Nothing", "Test"]

for c in GeneralListKeywords:
    City=c[0]
    km=c[1]
    tw=c[2]
    for Ti in TimeInterval:
        for K in EmojisList:
            KeywordsTweets_i= pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"{}" near:"{}" within:{}km {}'.format(K,City,km,Ti)).get_items(), int('{}'.format(tw))))
        if not KeywordsTweets_i.empty:
            KeywordsTweets_i['user_location'] = KeywordsTweets_i['user'].apply(lambda x: x['location'])
            KeywordsTweets_i['City'] = '{}'.format(City) #to chunck the df based on the city column
            KeywordsTweets_i['Search'] = 'ByKeywords' #To know the type of searching for this tweet, when concatenate all the files
            KeywordsTweets=pd.concat([KeywordsTweets,KeywordsTweets_i])  
        else:
            NoKeywordTweetList.append("{} Does not have Tweets with: - {} - Keyword in this Time Interval {}".format(City,K,Ti))
#All the Saudi Reigonal Tweets | Searching by Keywords 
KeywordsTweets.to_csv('KeywordsTweets.csv')
#File for each city and the missing Keywords:
NoKeywordsiTweetDF=pd.DataFrame(NoKeywordTweetList) #Check If we need to change it inot dataframe
NoKeywordsiTweetDF.to_csv("MissingKeywordsInTweets.csv")

now = datetime.now()
print("KEYWORDS: Ending Time =", now.strftime("%H:%M:%S"))

#******************[  End  :     By Keywords    ]************************

#........................................................................

#******************[ Start :     By #Hashtags   ]************************

now = datetime.now()
print("HASHTAGS: Starting Time =", now.strftime("%H:%M:%S"))

GeneralListHashtags=[('Riyadh','250','1000'), ('Jeddah','300','1000'), ('Dammam','200','1000'), ('Abha','150','500'), ('Jizan','150','500'), ('24.470901, 39.612236','100','500'), ('Buraidah','100','500'), ('Tabuk','100','500'), ('Hail','100','500'), ('Najran','50','500'), ('29.5,39.52236','50','500'), ('20.0125, 41.465278','50','500'), ('Arar','50','500')]
HashtagsList= ["#الشباب" , "#النصر" , "#الهلال" , "#الأهلي" , "#الاتحاد" , "#الدوري_ألسعودي" , "#التماسيح" , "#الطحالب" , "#النمور" , "#حضر" , "#بدو" , "#نسوية" , "#نسوي" , "#ذكورية" , "#ذكوري" , "#مستقلة" , "#حرة"]
HashtagsTweets=pd.DataFrame()
NoHashtagsTweetList=["Nothing", "Test"]

for c in GeneralListHashtags:
    City=c[0]
    km=c[1]
    tw=c[2]
    for Ti in TimeInterval:
        for H in EmojisList:
            HashtagsTweets_i= pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"{}" near:"{}" within:{}km {}'.format(H,City,km,Ti)).get_items(), int('{}'.format(tw))))
        if not HashtagsTweets_i.empty:
            HashtagsTweets_i['user_location'] = HashtagsTweets_i['user'].apply(lambda x: x['location'])
            HashtagsTweets_i['City'] = '{}'.format(City) #to chunck the df based on the city column
            HashtagsTweets_i['Search'] = 'ByHashtag' #To know the type of searching for this tweet, when concatenate all the files
            HashtagsTweets=pd.concat([HashtagsTweets,HashtagsTweets_i])  
        else:
            NoHashtagsTweetList.append("{} Does not have Tweets with - {} - Hashtag in this Time Interval {}".format(City,H,Ti))
#All the Saudi Reigonal Tweets | Searching by Hashtag 
HashtagsTweets.to_csv('HashtagsTweets.csv')
#File for each city and the missing Keywords:
NoKeywordsiTweetDF=pd.DataFrame(NoHashtagsTweetList) #Check If we need to change it inot dataframe
NoKeywordsiTweetDF.to_csv("MissingHashtagsInTweets.csv")

now = datetime.now()
print("HASHTAGS: Ending Time =", now.strftime("%H:%M:%S"))

#******************[  End  :     By #Hashtags   ]************************

#........................................................................


#****************[ Saudi DataSet Seperation Files]************************

SaudiTweetList=[GeneralTweets, EmojisTweets, KeywordsTweets, HashtagsTweets]
SaudiTweet= pd.concat(SaudiTweetList)
SaudiTweet.to_csv('SaudiTweet.csv')

#****************[ End of Collecting Process ]******************************
