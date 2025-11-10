import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'singin.settings')
django.setup()

from Users.models import Question, QuizSettings

# ایجاد تنظیمات آزمون
quiz_settings, created = QuizSettings.objects.get_or_create(
    id=1,
    defaults={
        'total_questions': 10,
        'points_per_correct': 1,
        'points_per_wrong': -1,
        'is_active': True
    }
)




questions = [
    {
        'text': 'کدام دریاچه، بزرگترین دریاچهٔ جهان محسوب می‌شود؟',
        'option1': 'دریاچه خزر',
        'option2': 'دریاچه سوپریور',
        'option3': 'دریاچه ویکتوریا',
        'option4': 'دریاچه بایکال',
        'correct_option': 1
    },
    {
        'text': 'معروف ترین اثر فرانز کافکا چیست؟',
        'option1': 'مسخ',
        'option2': 'قصر',
        'option3': 'محاکمه',
        'option4': 'آمریکا',
        'correct_option': 1
    },
    {
        'text': 'کدام کشور به عنوان "سرزمین طلوع خورشید" شناخته می‌شود؟',
        'option1': 'چین',
        'option2': 'کره جنوبی',
        'option3': 'ژاپن',
        'option4': 'تایلند',
        'correct_option': 3
    },
    {
        'text': 'عنصر شیمیایی با نماد Fe چیست؟',
        'option1': 'فلورین',
        'option2': 'فریم',
        'option3': 'آهن',
        'option4': 'فسفر',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این شهرها در ترکیه قرار دارد؟',
        'option1': 'دبی',
        'option2': 'باکو',
        'option3': 'ازمیر',
        'option4': 'تفلیس',
        'correct_option': 3
    },
    {
        'text': 'کدام اندام بدن انسان مسئول تولید انسولین است؟',
        'option1': 'کبد',
        'option2': 'لوزالمعده',
        'option3': 'کلیه',
        'option4': 'معده',
        'correct_option': 2
    },
    {
        'text': 'کدام سیاره دارای حلقه‌های مشخص و گسترده است؟',
        'option1': 'مشتری',
        'option2': 'زحل',
        'option3': 'اورانوس',
        'option4': 'نپتون',
        'correct_option': 2
    },
    {
        'text': 'نویسنده کتاب "صد سال تنهایی" کیست؟',
        'option1': 'پابلو نرودا',
        'option2': 'گابریل گارسیا مارکز',
        'option3': 'ماریو بارگاس یوسا',
        'option4': 'خورخه لوئیس بورخس',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک واحد اندازه‌گیری نیرو است؟',
        'option1': 'وات',
        'option2': 'نیوتن',
        'option3': 'ژول',
        'option4': 'پاسکال',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور استرالیا کدام شهر است؟',
        'option1': 'سیدنی',
        'option2': 'ملبورن',
        'option3': 'کانبرا',
        'option4': 'بریزبن',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این حیوانات کیسه‌دار است؟',
        'option1': 'سگ',
        'option2': 'کانگورو',
        'option3': 'فیل',
        'option4': 'میمون',
        'correct_option': 2
    },
    {
        'text': 'طولانی ترین رود جهان کدام است؟',
        'option1': 'آمازون',
        'option2': 'نیل',
        'option3': 'میسیسیپی',
        'option4': 'یانگتسه',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک سبک معماری است؟',
        'option1': 'رمانتیک',
        'option2': 'گوتیک',
        'option3': 'سورئال',
        'option4': 'امپرسیونیسم',
        'correct_option': 2
    },
    {
        'text': 'در کدام قاره کشور شیلی قرار دارد؟',
        'option1': 'آمریکای شمالی',
        'option2': 'آمریکای جنوبی',
        'option3': 'اروپا',
        'option4': 'آفریقا',
        'correct_option': 2
    },
    {
        'text': 'گاز اصلی تشکیل دهندهٔ جو زمین چیست؟',
        'option1': 'اکسیژن',
        'option2': 'نیتروژن',
        'option3': 'دی اکسید کربن',
        'option4': 'هیدروژن',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'پیانو',
        'option2': 'ویولن',
        'option3': 'فلوت',
        'option4': 'ساکسیفون',
        'correct_option': 2
    },
    {
        'text': 'مخترع تلفن کیست؟',
        'option1': 'توماس ادیسون',
        'option2': 'الکساندر گراهام بل',
        'option3': 'نیکولا تسلا',
        'option4': 'گالیله',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها بزرگترین بیابان جهان است؟',
        'option1': 'بیابان صحرا',
        'option2': 'بیابان عربستان',
        'option3': 'بیابان گبی',
        'option4': 'بیابان قطب جنوب',
        'correct_option': 4
    },
    {
        'text': 'پایتخت کشور کانادا کدام شهر است؟',
        'option1': 'تورنتو',
        'option2': 'ونکوور',
        'option3': 'مونترال',
        'option4': 'اتاوا',
        'correct_option': 4
    },
    {
        'text': 'کدام یک از این‌ها یک بیماری مسری است؟',
        'option1': 'دیابت',
        'option2': 'مالاریا',
        'option3': 'آرتروز',
        'option4': 'آسم',
        'correct_option': 2
    },
    {
        'text': 'سخنگوی هایک در فیلم "دزدان دریایی کارائیب" کیست؟',
        'option1': 'جانی دپ',
        'option2': 'اورلاندو بلوم',
        'option3': 'جفری راش',
        'option4': 'کیفر ساترلند',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع ابر است؟',
        'option1': 'سیروس',
        'option2': 'توفان',
        'option3': 'باران',
        'option4': 'باد',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Au چیست؟',
        'option1': 'نقره',
        'option2': 'مس',
        'option3': 'طلا',
        'option4': 'آلومینیوم',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'گلف',
        'option2': 'جودو',
        'option3': 'اسکی',
        'option4': 'شنا',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور برزیل کدام شهر است؟',
        'option1': 'ریو دو ژانیرو',
        'option2': 'سائو پائولو',
        'option3': 'برازیلیا',
        'option4': 'سالوادور',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک نوع سنگ آذرین است؟',
        'option1': 'گرانیت',
        'option2': 'مرمر',
        'option3': 'شیست',
        'option4': 'سنگ آهک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی نظریه نسبیت را ارائه داد؟',
        'option1': 'نیوتن',
        'option2': 'گالیله',
        'option3': 'انیشتین',
        'option4': 'هاوکینگ',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها بزرگترین ماهی جهان است؟',
        'option1': 'کوسه سفید',
        'option2': 'کوسه نهنگ',
        'option3': 'ماهی مرکب',
        'option4': 'ماهی تن',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور ایتالیا کدام شهر است؟',
        'option1': 'میلان',
        'option2': 'ونیز',
        'option3': 'ناپل',
        'option4': 'رم',
        'correct_option': 4
    },
    {
        'text': 'کدام یک از این‌ها یک پایتخت اروپایی است؟',
        'option1': 'داکار',
        'option2': 'لیما',
        'option3': 'بوداپست',
        'option4': 'مانیل',
        'correct_option': 3
    },
    {
        'text': 'عنصر شیمیایی با نماد Hg چیست؟',
        'option1': 'هلیوم',
        'option2': 'هیدروژن',
        'option3': 'جیوه',
        'option4': 'هافنیم',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'گیتار',
        'option2': 'درام',
        'option3': 'ترومپت',
        'option4': 'ویولن سل',
        'correct_option': 3
    },
    {
        'text': 'چه کسی تابلوی "شب پرستاره" را نقاشی کرد؟',
        'option1': 'پابلو پیکاسو',
        'option2': 'ون گوگ',
        'option3': 'سالوادور دالی',
        'option4': 'کلود مونه',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک زبان برنامه‌نویسی است؟',
        'option1': 'اکسل',
        'option2': 'جاوا',
        'option3': 'فتوشاپ',
        'option4': 'پاورپوینت',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور هند کدام شهر است؟',
        'option1': 'بمبئی',
        'option2': 'دهلی نو',
        'option3': 'کلکته',
        'option4': 'چنای',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'دلفین',
        'option3': 'عقاب',
        'option4': 'مار',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Na چیست؟',
        'option1': 'نیتروژن',
        'option2': 'نئون',
        'option3': 'سدیم',
        'option4': 'نیکل',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'رئالیسم',
        'option2': 'جاز',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 2
    },
    {
        'text': 'چه کسی نمایشنامه "هملت" را نوشت؟',
        'option1': 'اسکار وایلد',
        'option2': 'ویلیام شکسپیر',
        'option3': 'چارلز دیکنز',
        'option4': 'جین آستن',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک کشور جزیره‌ای است؟',
        'option1': 'مغولستان',
        'option2': 'سوئیس',
        'option3': 'اندونزی',
        'option4': 'لهستان',
        'correct_option': 3
    },
    {
        'text': 'عنصر شیمیایی با نماد K چیست؟',
        'option1': 'کریپتون',
        'option2': 'کبالت',
        'option3': 'پتاسیم',
        'option4': 'کادمیوم',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش تیمی است؟',
        'option1': 'تنیس',
        'option2': 'بسکتبال',
        'option3': 'گلف',
        'option4': 'شنا',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور چین کدام شهر است؟',
        'option1': 'شانگهای',
        'option2': 'پکن',
        'option3': 'گوانگژو',
        'option4': 'هنگ کنگ',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک سیاره خاکی است؟',
        'option1': 'مشتری',
        'option2': 'زهره',
        'option3': 'اورانوس',
        'option4': 'نپتون',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ag چیست؟',
        'option1': 'آرگون',
        'option2': 'نقره',
        'option3': 'طلا',
        'option4': 'آلومینیوم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک درخت میوه است؟',
        'option1': 'بلوط',
        'option2': 'سیب',
        'option3': 'صنوبر',
        'option4': 'کاج',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "آنا کارنینا" را نوشت؟',
        'option1': 'فئودور داستایفسکی',
        'option2': 'لئو تولستوی',
        'option3': 'آنتون چخوف',
        'option4': 'الکساندر پوشکین',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'ونزوئلا',
        'option2': 'نیجریه',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Cu چیست؟',
        'option1': 'کبالت',
        'option2': 'کروم',
        'option3': 'مس',
        'option4': 'کلسیم',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک ابزار موسیقی کوبه‌ای است؟',
        'option1': 'پیانو',
        'option2': 'درام',
        'option3': 'ترومبون',
        'option4': 'کلارینت',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور آلمان کدام شهر است؟',
        'option1': 'مونیخ',
        'option2': 'فرانکفورت',
        'option3': 'برلین',
        'option4': 'هامبورگ',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک نوع ابر است؟',
        'option1': 'کومولوس',
        'option2': 'سیکلون',
        'option3': 'سونامی',
        'option4': 'توفند',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Pb چیست؟',
        'option1': 'پلاتین',
        'option2': 'پالادیم',
        'option3': 'سرب',
        'option4': 'فسفر',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک سبک رقص است؟',
        'option1': 'رئالیسم',
        'option2': 'باله',
        'option3': 'کوبیسم',
        'option4': 'امپرسیونیسم',
        'correct_option': 2
    },
    {
        'text': 'چه کسی نظریه تکامل را ارائه داد؟',
        'option1': 'چارلز داروین',
        'option2': 'آلبرت انیشتین',
        'option3': 'آیزاک نیوتن',
        'option4': 'لوئی پاستور',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اسکاندیناویایی است؟',
        'option1': 'اسپانیا',
        'option2': 'سوئد',
        'option3': 'لهستان',
        'option4': 'اتریش',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Sn چیست؟',
        'option1': 'استرانسیوم',
        'option2': 'سلنیوم',
        'option3': 'قلع',
        'option4': 'گوگرد',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'فوتبال',
        'option2': 'قایقرانی',
        'option3': 'والیبال',
        'option4': 'بسکتبال',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور فرانسه کدام شهر است؟',
        'option1': 'مارسی',
        'option2': 'لیون',
        'option3': 'پاریس',
        'option4': 'نیس',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک نوع سنگ رسوبی است؟',
        'option1': 'گرانیت',
        'option2': 'بازالت',
        'option3': 'سنگ آهک',
        'option4': 'مرمر',
        'correct_option': 3
    },
    {
        'text': 'عنصر شیمیایی با نماد Zn چیست؟',
        'option1': 'زیرکونیوم',
        'option2': 'روی',
        'option3': 'زنون',
        'option4': 'زیمبابوه',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ساز کلاویه‌ای است؟',
        'option1': 'گیتار',
        'option2': 'درام',
        'option3': 'پیانو',
        'option4': 'ترومپت',
        'correct_option': 3
    },
    {
        'text': 'چه کسی مجسمه "داود" را خلق کرد؟',
        'option1': 'لئوناردو داوینچی',
        'option2': 'میکل آنژ',
        'option3': 'دوناتلو',
        'option4': 'رافائل',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک کشور خاورمیانه است؟',
        'option1': 'مکزیک',
        'option2': 'عربستان سعودی',
        'option3': 'برزیل',
        'option4': 'هند',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ni چیست؟',
        'option1': 'نیتروژن',
        'option2': 'نیکل',
        'option3': 'نئون',
        'option4': 'ناتریوم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش زمستانی است؟',
        'option1': 'شنا',
        'option2': 'اسکی',
        'option3': 'تنیس',
        'option4': 'دوچرخه سواری',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور روسیه کدام شهر است؟',
        'option1': 'سن پترزبورگ',
        'option2': 'مسکو',
        'option3': 'نووسیبیرسک',
        'option4': 'یکاترینبورگ',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک پستاندار پرنده است؟',
        'option1': 'پنگوئن',
        'option2': 'خفاش',
        'option3': 'شترمرغ',
        'option4': 'عقاب',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ca چیست؟',
        'option1': 'کربن',
        'option2': 'کلر',
        'option3': 'کلسیم',
        'option4': 'کروم',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک سبک هنری است؟',
        'option1': 'سورئالیسم',
        'option2': 'سونات',
        'option3': 'سمفونی',
        'option4': 'اپرا',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی نهم بتهوون را ساخت؟',
        'option1': 'موتزارت',
        'option2': 'باخ',
        'option3': 'بتهوون',
        'option4': 'چایکوفسکی',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای مرکزی است؟',
        'option1': 'کاستاریکا',
        'option2': 'کلمبیا',
        'option3': 'ونزوئلا',
        'option4': 'پرو',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Mg چیست؟',
        'option1': 'منگنز',
        'option2': 'منیزیم',
        'option3': 'مولیبدن',
        'option4': 'جیوه',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'کاراته',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور اسپانیا کدام شهر است؟',
        'option1': 'بارسلونا',
        'option2': 'مادرید',
        'option3': 'والنسیا',
        'option4': 'سویل',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع قارچ است؟',
        'option1': 'قارچ خوراکی',
        'option2': 'سرخس',
        'option3': 'خزه',
        'option4': 'جلبک',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Al چیست؟',
        'option1': 'آرگون',
        'option2': 'آنتیموان',
        'option3': 'آلومینیوم',
        'option4': 'استرانسیوم',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی آرشه‌ای است؟',
        'option1': 'گیتار',
        'option2': 'ویولن',
        'option3': 'پیانو',
        'option4': 'فلوت',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "گرنیکا" را نقاشی کرد؟',
        'option1': 'پابلو پیکاسو',
        'option2': 'سالوادور دالی',
        'option3': 'ون گوگ',
        'option4': 'کلود مونه',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اقیانوسیه است؟',
        'option1': 'نیوزیلند',
        'option2': 'ژاپن',
        'option3': 'فیلیپین',
        'option4': 'اندونزی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Si چیست؟',
        'option1': 'گوگرد',
        'option2': 'سلنیوم',
        'option3': 'سیلیسیم',
        'option4': 'استرانسیوم',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'فوتبال',
        'option2': 'تنیس',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور آرژانتین کدام شهر است؟',
        'option1': 'ریو دو ژانیرو',
        'option2': 'سائو پائولو',
        'option3': 'بوئنوس آیرس',
        'option4': 'لیما',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک نوع ابر است؟',
        'option1': 'استراتوس',
        'option2': 'توفان',
        'option3': 'گردباد',
        'option4': 'سونامی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد P چیست؟',
        'option1': 'پلاتین',
        'option2': 'فسفر',
        'option3': 'پالادیم',
        'option4': 'پتاسیم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک سبک معماری است؟',
        'option1': 'رمانتیک',
        'option2': 'باروک',
        'option3': 'سورئال',
        'option4': 'امپرسیونیسم',
        'correct_option': 2
    },
    {
        'text': 'چه کسی نظریه روانکاوی را توسعه داد؟',
        'option1': 'زیگموند فروید',
        'option2': 'کارل یونگ',
        'option3': 'اریک اریکسون',
        'option4': 'آلفرد آدلر',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'مصر',
        'option2': 'ویتنام',
        'option3': 'کنیا',
        'option4': 'مراکش',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد S چیست؟',
        'option1': 'سلنیوم',
        'option2': 'گوگرد',
        'option3': 'سیلیسیم',
        'option4': 'استرانسیوم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی چوبی است؟',
        'option1': 'ترومپت',
        'option2': 'فلوت',
        'option3': 'ترومبون',
        'option4': 'توبا',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور مکزیک کدام شهر است؟',
        'option1': 'گوادالاخارا',
        'option2': 'مکزیکو سیتی',
        'option3': 'مونتری',
        'option4': 'پوئبلا',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'پنگوئن',
        'option3': 'دلفین',
        'option4': 'وال',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Cl چیست؟',
        'option1': 'کلسیم',
        'option2': 'کلر',
        'option3': 'کروم',
        'option4': 'کبالت',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک سبک رقص است؟',
        'option1': 'تانگو',
        'option2': 'سونات',
        'option3': 'سمفونی',
        'option4': 'اپرا',
        'correct_option': 1
    },
    {
        'text': 'چه کسی نمایشنامه "مادام باترفلای" را نوشت؟',
        'option1': 'جاکومو پوچینی',
        'option2': 'جوزپه وردی',
        'option3': 'ریشارد واگنر',
        'option4': 'ولفگانگ آمادئوس موتزارت',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'پرو',
        'option2': 'لهستان',
        'option3': 'تانزانیا',
        'option4': 'فیلیپین',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ar چیست؟',
        'option1': 'آرگون',
        'option2': 'آرسنیک',
        'option3': 'آنتیموان',
        'option4': 'آلومینیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'شنا',
        'option2': 'فوتبال',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور ترکیه کدام شهر است؟',
        'option1': 'استانبول',
        'option2': 'آنکارا',
        'option3': 'ازمیر',
        'option4': 'بورسا',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'کفشدوزک',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Kr چیست؟',
        'option1': 'کربن',
        'option2': 'کریپتون',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ساز کوبه‌ای است؟',
        'option1': 'پیانو',
        'option2': 'گیتار',
        'option3': 'تمبرین',
        'option4': 'فلوت',
        'correct_option': 3
    },
    {
        'text': 'چه کسی کتاب "بینوایان" را نوشت؟',
        'option1': 'الکساندر دوما',
        'option2': 'ویکتور هوگو',
        'option3': 'گوستاو فلوبر',
        'option4': 'امیل زولا',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای جنوبی است؟',
        'option1': 'پرو',
        'option2': 'کاستاریکا',
        'option3': 'پاناما',
        'option4': 'گواتمالا',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Br چیست؟',
        'option1': 'بور',
        'option2': 'برم',
        'option3': 'بیسموت',
        'option4': 'باریم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش المپیکی است؟',
        'option1': 'شطرنج',
        'option2': 'پرش ارتفاع',
        'option3': 'بیلیارد',
        'option4': 'کریکت',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور کره جنوبی کدام شهر است؟',
        'option1': 'بوسان',
        'option2': 'سئول',
        'option3': 'اینچئون',
        'option4': 'دائجون',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'کروکودیل',
        'option2': 'نهنگ',
        'option3': 'مار',
        'option4': 'قورباغه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد I چیست؟',
        'option1': 'ایریدیم',
        'option2': 'ید',
        'option3': 'ایندیم',
        'option4': 'آهن',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'رئالیسم',
        'option2': 'رپ',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 2
    },
    {
        'text': 'چه کسی سمفونی "فصول" را ساخت؟',
        'option1': 'آنتونیو ویوالدی',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'کنیا',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Xe چیست؟',
        'option1': 'زنون',
        'option2': 'زیرکونیوم',
        'option3': 'روی',
        'option4': 'ایریدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'تکواندو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور یونان کدام شهر است؟',
        'option1': 'تسالونیکی',
        'option2': 'آتن',
        'option3': 'پاتراس',
        'option4': 'ایراکلیون',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع ماهی است؟',
        'option1': 'دلفین',
        'option2': 'قزل آلا',
        'option3': 'وال',
        'option4': 'کوسه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Rn چیست؟',
        'option1': 'رادون',
        'option2': 'رادیم',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'هارپ',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "جیغ" را نقاشی کرد؟',
        'option1': 'ادوارد مونک',
        'option2': 'ون گوگ',
        'option3': 'پل سزان',
        'option4': 'پل گوگن',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'پرتغال',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد U چیست؟',
        'option1': 'اورانیوم',
        'option2': 'اوپال',
        'option3': 'اولمین',
        'option4': 'اورت',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'والیبال',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور مصر کدام شهر است؟',
        'option1': 'اسکندریه',
        'option2': 'قاهره',
        'option3': 'جیزه',
        'option4': 'سوئز',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'شاهین',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Pu چیست؟',
        'option1': 'پلاتین',
        'option2': 'پلوتونیوم',
        'option3': 'پالادیم',
        'option4': 'پروتاکتینیم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'ویولن',
        'option2': 'کلارینت',
        'option3': 'گیتار',
        'option4': 'پیانو',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "دن کیشوت" را نوشت؟',
        'option1': 'میکل دو سروانتس',
        'option2': 'ویکتور هوگو',
        'option3': 'لئو تولستوی',
        'option4': 'فئودور داستایفسکی',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'تایلند',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نمod Am چیست؟',
        'option1': 'امریسیم',
        'option2': 'آنتیموان',
        'option3': 'آرسنیک',
        'option4': 'استرانسیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'شنا',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'تنیس',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور اندونزی کدام شهر است؟',
        'option1': 'جاکارتا',
        'option2': 'سورابایا',
        'option3': 'باندونگ',
        'option4': 'مدان',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'گوریل',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Cm چیست؟',
        'option1': 'کربن',
        'option2': 'کوریم',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'بلوز',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "شگفت انگیز" را ساخت؟',
        'option1': 'هکتور برلیوز',
        'option2': 'یوهانس برامس',
        'option3': 'فرانتس شوبرت',
        'option4': 'فلیکس مندلسون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'بلژیک',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Bk چیست؟',
        'option1': 'برکلیم',
        'option2': 'بور',
        'option3': 'بیسموت',
        'option4': 'باریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'بدمینتون',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور آفریقای جنوبی کدام شهر است؟',
        'option1': 'ژوهانسبورگ',
        'option2': 'کیپ تاون',
        'option3': 'پرتوریا',
        'option4': 'دوربان',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'مورچه',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Cf چیست؟',
        'option1': 'کالیفرنیم',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز کوبه‌ای است؟',
        'option1': 'سنج',
        'option2': 'پیانو',
        'option3': 'گیتار',
        'option4': 'فلوت',
        'correct_option': 1
    },
    {
        'text': 'چه کسی کتاب "غرور و تعصب" را نوشت؟',
        'option1': 'جین آستن',
        'option2': 'شارلوت برونته',
        'option3': 'امیلی برونته',
        'option4': 'ویرجینیا وولف',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای شمالی است؟',
        'option1': 'کانادا',
        'option2': 'برزیل',
        'option3': 'آرژانتین',
        'option4': 'شیلی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Es چیست؟',
        'option1': 'انیشتینیم',
        'option2': 'اربیوم',
        'option3': 'ایتریم',
        'option4': 'یوروپیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش المپیکی است؟',
        'option1': 'پرش با نیزه',
        'option2': 'شطرنج',
        'option3': 'بیلیارد',
        'option4': 'کریکت',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور نروژ کدام شهر است؟',
        'option1': 'اسلو',
        'option2': 'برگن',
        'option3': 'استاوانگر',
        'option4': 'تروندهایم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'فک',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Fm چیست؟',
        'option1': 'فرمیم',
        'option2': 'فلورین',
        'option3': 'فاسفور',
        'option4': 'فریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'هوی متال',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "ناتمام" را ساخت؟',
        'option1': 'فرانتس شوبرت',
        'option2': 'یوهانس برامس',
        'option3': 'فلیکس مندلسون',
        'option4': 'رابرت شومان',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'مالزی',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Md چیست؟',
        'option1': 'مندلیفیم',
        'option2': 'منگنز',
        'option3': 'مولیبدن',
        'option4': 'مس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'کونگ فو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور سوئد کدام شهر است؟',
        'option1': 'گوتنبرگ',
        'option2': 'استکهلم',
        'option3': 'مالمو',
        'option4': 'اوپسالا',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'بلبل',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد No چیست؟',
        'option1': 'نوبلیم',
        'option2': 'نیکل',
        'option3': 'نئون',
        'option4': 'ناتریوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'ویولن سل',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "نگهبان شب" را نقاشی کرد؟',
        'option1': 'رامبرانت',
        'option2': 'ون گوگ',
        'option3': 'پل سزان',
        'option4': 'پل گوگن',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'فنلاند',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Lr چیست؟',
        'option1': 'لارنسیم',
        'option2': 'لوتتیم',
        'option3': 'لیتیم',
        'option4': 'سرب',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'هاکی',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور دانمارک کدام شهر است؟',
        'option1': 'کپنهاگ',
        'option2': 'آرهوس',
        'option3': 'ادنسه',
        'option4': 'آلبورگ',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'زنبور عسل',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Rf چیست؟',
        'option1': 'رادرفوردیم',
        'option2': 'رادیم',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'ویولن',
        'option2': 'ساکسیفون',
        'option3': 'گیتار',
        'option4': 'پیانو',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "مادام بوواری" را نوشت؟',
        'option1': 'گوستاو فلوبر',
        'option2': 'امیل زولا',
        'option3': 'آناتول فرانس',
        'option4': 'گی دو موپاسان',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای جنوبی است؟',
        'option1': 'کلمبیا',
        'option2': 'کاستاریکا',
        'option3': 'پاناما',
        'option4': 'گواتمالا',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Db چیست؟',
        'option1': 'دوبنیم',
        'option2': 'دیسپروزیم',
        'option3': 'دارمشتاتیم',
        'option4': 'ديسپلاسيم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'قایقرانی بادبانی',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'تنیس',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور لهستان کدام شهر است؟',
        'option1': 'کراکوف',
        'option2': 'ورشو',
        'option3': 'ووج',
        'option4': 'پوزنان',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'کرگدن',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Sg چیست؟',
        'option1': 'سیبورگیوم',
        'option2': 'سلنیوم',
        'option3': 'سیلیسیم',
        'option4': 'استرانسیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'فانک',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "پاستورال" را ساخت؟',
        'option1': 'لودویگ فان بتهوون',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'فرانتس شوبرت',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'غنا',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Bh چیست؟',
        'option1': 'بوهریوم',
        'option2': 'بور',
        'option3': 'بیسموت',
        'option4': 'باریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'پینگ پنگ',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور مجارستان کدام شهر است؟',
        'option1': 'بوداپست',
        'option2': 'دبرسن',
        'option3': 'سگد',
        'option4': 'پچ',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'قرقاول',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Hs چیست؟',
        'option1': 'هاسیم',
        'option2': 'هلیوم',
        'option3': 'هیدروژن',
        'option4': 'هافنیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز کوبه‌ای است؟',
        'option1': 'طبلا',
        'option2': 'پیانو',
        'option3': 'گیتار',
        'option4': 'فلوت',
        'correct_option': 1
    },
    {
        'text': 'چه کسی کتاب "ناتور دشت" را نوشت؟',
        'option1': 'جروم دیوید سلینجر',
        'option2': 'ارنست همینگوی',
        'option3': 'اف اسکات فیتزجرالد',
        'option4': 'ویلیام فاکنر',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اقیانوسیه است؟',
        'option1': 'فیجی',
        'option2': 'ژاپن',
        'option3': 'فیلیپین',
        'option4': 'اندونزی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Mt چیست؟',
        'option1': 'مایتنریم',
        'option2': 'منگنز',
        'option3': 'مولیبدن',
        'option4': 'مس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش المپیکی است؟',
        'option1': 'پرتاب نیزه',
        'option2': 'شطرنج',
        'option3': 'بیلیارد',
        'option4': 'کریکت',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور جمهوری چک کدام شهر است؟',
        'option1': 'پراگ',
        'option2': 'برنو',
        'option3': 'استراوا',
        'option4': 'پلزن',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'گراز دریایی',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ds چیست؟',
        'option1': 'دارمشتاتیم',
        'option2': 'دیسپروزیم',
        'option3': 'دوبنیم',
        'option4': 'ديسپلاسيم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'دیسکو',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "از دنیای جدید" را ساخت؟',
        'option1': 'آنتونین دورژاک',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'سنگاپور',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Rg چیست؟',
        'option1': 'رونتگنیم',
        'option2': 'رادیم',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'جوجیتسو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور اتریش کدام شهر است؟',
        'option1': 'وین',
        'option2': 'گراتس',
        'option3': 'لینتس',
        'option4': 'سالزبورگ',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'سنجاقک',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Cn چیست؟',
        'option1': 'کوپرنیسیم',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'کنترباس',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "آفرینش آدم" را نقاشی کرد؟',
        'option1': 'میکل آنژ',
        'option2': 'لئوناردو داوینچی',
        'option3': 'رافائل',
        'option4': 'دوناتلو',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'سوئیس',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Nh چیست؟',
        'option1': 'نیهونیم',
        'option2': 'نیکل',
        'option3': 'نئون',
        'option4': 'ناتریوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'راگبی',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور رومانی کدام شهر است؟',
        'option1': 'بخارست',
        'option2': 'کلوژ-نپوکا',
        'option3': 'تیمیشوارا',
        'option4': 'یاشی',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'گاومیش',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Fl چیست؟',
        'option1': 'فلروویوم',
        'option2': 'فلورین',
        'option3': 'فاسفور',
        'option4': 'فریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'سول',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "کارمینا بورانا" را ساخت؟',
        'option1': 'کارل اورف',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'ساحل عاج',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Mc چیست؟',
        'option1': 'مسکوویوم',
        'option2': 'منگنز',
        'option3': 'مولیبدن',
        'option4': 'مس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'اسکواش',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور بلژیک کدام شهر است؟',
        'option1': 'بروکسل',
        'option2': 'آنتورپ',
        'option3': 'گنت',
        'option4': 'لیژ',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'قناری',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Lv چیست؟',
        'option1': 'لیورموریوم',
        'option2': 'لوتتیم',
        'option3': 'لیتیم',
        'option4': 'سرب',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'ویولن',
        'option2': 'ابوا',
        'option3': 'گیتار',
        'option4': 'پیانو',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "در جستجوی زمان از دست رفته" را نوشت؟',
        'option1': 'مارسل پروست',
        'option2': 'ژان پل سارتر',
        'option3': 'آلبر کامو',
        'option4': 'آندره ژید',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای شمالی است؟',
        'option1': 'مکزیک',
        'option2': 'برزیل',
        'option3': 'آرژانتین',
        'option4': 'شیلی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Ts چیست؟',
        'option1': 'تننسین',
        'option2': 'تیتانیوم',
        'option3': 'تالیم',
        'option4': 'تلوریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'واترپلو',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'تنیس',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور پرتغال کدام شهر است؟',
        'option1': 'لیسبون',
        'option2': 'پورتو',
        'option3': 'کاشکایش',
        'option4': 'براگا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'نهنگ قاتل',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Og چیست؟',
        'option1': 'اوگانسون',
        'option2': 'اکسیژن',
        'option3': 'اسمیم',
        'option4': 'اروپیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'هیپ هاپ',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "فانتاستیک" را ساخت؟',
        'option1': 'هکتور برلیوز',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'کامبوج',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد He چیست؟',
        'option1': 'هلیوم',
        'option2': 'هیدروژن',
        'option3': 'هافنیم',
        'option4': 'هولمیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'موای تای',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور ایرلند کدام شهر است؟',
        'option1': 'دوبلین',
        'option2': 'کورک',
        'option3': 'گالوی',
        'option4': 'لیمریک',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'ملخ',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ne چیست؟',
        'option1': 'نئون',
        'option2': 'نیکل',
        'option3': 'ناتریوم',
        'option4': 'نیوبیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'ویولا',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "دختری با گوشواره مروارید" را نقاشی کرد؟',
        'option1': 'یوهانس ورمر',
        'option2': 'رامبرانت',
        'option3': 'پیر آگوست رنوار',
        'option4': 'ادگار دگا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'اسلوونی',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Ar چیست؟',
        'option1': 'آرگون',
        'option2': 'آرسنیک',
        'option3': 'آنتیموان',
        'option4': 'آلومینیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'کریکت',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور اسکاتلند کدام شهر است؟',
        'option1': 'ادینبورگ',
        'option2': 'گلاسگو',
        'option3': 'ابردین',
        'option4': 'دندی',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'گوزن',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Kr چیست؟',
        'option1': 'کریپتون',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'ریتم اند بلوز',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "اپرای فضا" را ساخت؟',
        'option1': 'گوستاو هولست',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'تانزانیا',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Xe چیست؟',
        'option1': 'زنون',
        'option2': 'زیرکونیوم',
        'option3': 'روی',
        'option4': 'ایریدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'تنیس روی میز',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور ولز کدام شهر است؟',
        'option1': 'کاردیف',
        'option2': 'سوانزی',
        'option3': 'نیوپورت',
        'option4': 'بانگور',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'پلیکان',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Rn چیست؟',
        'option1': 'رادون',
        'option2': 'رادیم',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز کوبه‌ای است؟',
        'option1': 'دف',
        'option2': 'پیانو',
        'option3': 'گیتار',
        'option4': 'فلوت',
        'correct_option': 1
    },
    {
        'text': 'چه کسی کتاب "ارباب حلقه‌ها" را نوشت؟',
        'option1': 'جی. آر. آر. تالکین',
        'option2': 'سی. اس. لوئیس',
        'option3': 'جی. کی. رولینگ',
        'option4': 'آر. آر. مارتین',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اقیانوسیه است؟',
        'option1': 'پاپوآ گینه نو',
        'option2': 'ژاپن',
        'option3': 'فیلیپین',
        'option4': 'اندونزی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Fr چیست؟',
        'option1': 'فرانسیوم',
        'option2': 'فلورین',
        'option3': 'فاسفور',
        'option4': 'فریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش المپیکی است؟',
        'option1': 'پرش سه گام',
        'option2': 'شطرنج',
        'option3': 'بیلیارد',
        'option4': 'کریکت',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور اسلواکی کدام شهر است؟',
        'option1': 'براتیسلاوا',
        'option2': 'کوشیتسه',
        'option3': 'پرشوف',
        'option4': 'ژیلینا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'گراز دریایی',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ra چیست؟',
        'option1': 'رادیم',
        'option2': 'رادون',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'کانتری',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "عروسک خیمه شب بازی" را ساخت؟',
        'option1': 'لئو دلیب',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'لائوس',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Ac چیست؟',
        'option1': 'آکتینیم',
        'option2': 'آرسنیک',
        'option3': 'آنتیموان',
        'option4': 'آلومینیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'کندو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور کرواسی کدام شهر است؟',
        'option1': 'زاگرب',
        'option2': 'اسپلیت',
        'option3': 'رییکا',
        'option4': 'اوسییک',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'مگس',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Th چیست؟',
        'option1': 'توریم',
        'option2': 'تیتانیوم',
        'option3': 'تالیم',
        'option4': 'تلوریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'چلو',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "ناهار در چمنزار" را نقاشی کرد؟',
        'option1': 'ادوار مانه',
        'option2': 'کلود مونه',
        'option3': 'پیر آگوست رنوار',
        'option4': 'ادگار دگا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'لتونی',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Pa چیست؟',
        'option1': 'پروتاکتینیم',
        'option2': 'پالادیم',
        'option3': 'پلاتین',
        'option4': 'پتاسیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'هندبال',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور لیتوانی کدام شهر است؟',
        'option1': 'ویلنیوس',
        'option2': 'کاوناس',
        'option3': 'کلایپدا',
        'option4': 'شاولیای',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'گورکن',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Np چیست؟',
        'option1': 'نپتونیوم',
        'option2': 'نیکل',
        'option3': 'نئون',
        'option4': 'ناتریوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'رگی',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "شب روی کوه سنگی" را ساخت؟',
        'option1': 'مودست موسورگسکی',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'اوگاندا',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Pu چیست؟',
        'option1': 'پلوتونیوم',
        'option2': 'پالادیم',
        'option3': 'پلاتین',
        'option4': 'پتاسیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'بدمنتون',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور استونی کدام شهر است؟',
        'option1': 'تالین',
        'option2': 'تارتو',
        'option3': 'ناروا',
        'option4': 'پارنو',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'فلامینگو',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Am چیست؟',
        'option1': 'امریسیم',
        'option2': 'آنتیموان',
        'option3': 'آرسنیک',
        'option4': 'استرانسیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'ویولن',
        'option2': 'باسون',
        'option3': 'گیتار',
        'option4': 'پیانو',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "ناخدا هسته" را نوشت؟',
        'option1': 'هرمان ملویل',
        'option2': 'ارنست همینگوی',
        'option3': 'مارک تواین',
        'option4': 'جک لندن',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای شمالی است؟',
        'option1': 'کاستاریکا',
        'option2': 'برزیل',
        'option3': 'آرژانتین',
        'option4': 'شیلی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Cm چیست؟',
        'option1': 'کوریم',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'شیرجه',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'تنیس',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور بلغارستان کدام شهر است؟',
        'option1': 'صوفیه',
        'option2': 'پلوودیف',
        'option3': 'وارنا',
        'option4': 'بورگاس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'نهنگ آبی',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Bk چیست؟',
        'option1': 'برکلیم',
        'option2': 'بور',
        'option3': 'بیسموت',
        'option4': 'باریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'پانک راک',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "رومئو و ژولیت" را ساخت؟',
        'option1': 'هکتور برلیوز',
        'option2': 'پیوتر ایلیچ چایکوفسکی',
        'option3': 'سرگئی پروکفیف',
        'option4': 'ایگور استراوینسکی',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'میانمار',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Cf چیست؟',
        'option1': 'کالیفرنیم',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'آیکیدو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور صربستان کدام شهر است؟',
        'option1': 'بلگراد',
        'option2': 'نوی ساد',
        'option3': 'نیس',
        'option4': 'کراگویواتس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'سوسک',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Es چیست؟',
        'option1': 'انیشتینیم',
        'option2': 'اربیوم',
        'option3': 'ایتریم',
        'option4': 'یوروپیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'عود',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "مردی با کلاه لبه دار" را نقاشی کرد؟',
        'option1': 'رامبرانت',
        'option2': 'ون گوگ',
        'option3': 'پل سزان',
        'option4': 'پل گوگن',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'مونته نگرو',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Fm چیست؟',
        'option1': 'فرمیم',
        'option2': 'فلورین',
        'option3': 'فاسفور',
        'option4': 'فریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'بازی های محلی',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور بوسنی و هرزگوین کدام شهر است؟',
        'option1': 'سارایوو',
        'option2': 'بانیا لوکا',
        'option3': 'موستار',
        'option4': 'توزلا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'سمور',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Md چیست؟',
        'option1': 'مندلیفیم',
        'option2': 'منگنز',
        'option3': 'مولیبدن',
        'option4': 'مس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'الکترونیک',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "پولوفتسیان رقص" را ساخت؟',
        'option1': 'الکساندر بورودین',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'زیمبابوه',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد No چیست؟',
        'option1': 'نوبلیم',
        'option2': 'نیکل',
        'option3': 'نئون',
        'option4': 'ناتریوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'تنیس بیچ',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور مقدونیه شمالی کدام شهر است؟',
        'option1': 'اسکوپیه',
        'option2': 'بیتولا',
        'option3': 'کومانوفو',
        'option4': 'پریlep',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'طاووس',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Lr چیست？',
        'option1': 'لارنسیم',
        'option2': 'لوتتیم',
        'option3': 'لیتیم',
        'option4': 'سرب',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'ویولن',
        'option2': 'فاگوت',
        'option3': 'گیتار',
        'option4': 'پیانو',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "صد سال تنهایی" را نوشت؟',
        'option1': 'گابریل گارسیا مارکز',
        'option2': 'ماریو بارگاس یوسا',
        'option3': 'خورخه لوئیس بورخس',
        'option4': 'پابلو نرودا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای جنوبی است؟',
        'option1': 'اروگوئه',
        'option2': 'کاستاریکا',
        'option3': 'پاناما',
        'option4': 'گواتمالا',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Rf چیست؟',
        'option1': 'رادرفوردیم',
        'option2': 'رادیم',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'واتراسکی',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'تنیس',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور آلبانی کدام شهر است？',
        'option1': 'تیرانا',
        'option2': 'دورس',
        'option3': 'ولوره',
        'option4': 'شکودر',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'نهنگ خاکستری',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Db چیست？',
        'option1': 'دوبنیم',
        'option2': 'دیسپروزیم',
        'option3': 'دارمشتاتیم',
        'option4': 'ديسپلاسيم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'متال',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "شهرزاد" را ساخت؟',
        'option1': 'نیکلای ریمسکی-کورساکف',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'بنگلادش',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Sg چیست？',
        'option1': 'سیبورگیوم',
        'option2': 'سلنیوم',
        'option3': 'سیلیسیم',
        'option4': 'استرانسیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'هاپکیدو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور مالت کدام شهر است？',
        'option1': 'والتا',
        'option2': 'بیرکیرکارا',
        'option3': 'اسلیما',
        'option4': 'ربات',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'پشه',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Bh چیست؟',
        'option1': 'بوهریوم',
        'option2': 'بور',
        'option3': 'بیسموت',
        'option4': 'باریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'سیتر',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "تابستان" را نقاشی کرد؟',
        'option1': 'جوزپه آرچیمبولدو',
        'option2': 'لئوناردو داوینچی',
        'option3': 'رافائل',
        'option4': 'میکل آنژ',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'آندورا',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Hs چیست؟',
        'option1': 'هاسیم',
        'option2': 'هلیوم',
        'option3': 'هیدروژن',
        'option4': 'هافنیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'پولو',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور ایسلند کدام شهر است؟',
        'option1': 'ریکیاویک',
        'option2': 'کپاووگور',
        'option3': 'هافنارفیوردور',
        'option4': 'آکوریری',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'راسو',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Mt چیست؟',
        'option1': 'مایتنریم',
        'option2': 'منگنز',
        'option3': 'مولیبدن',
        'option4': 'مس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'ایندی راک',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "پتروشکا" را ساخت؟',
        'option1': 'ایگور استراوینسکی',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'سودان',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Ds چیست؟',
        'option1': 'دارمشتاتیم',
        'option2': 'دیسپروزیم',
        'option3': 'دوبنیم',
        'option4': 'ديسپلاسيم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'پدل تنیس',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور لوکزامبورگ کدام شهر است؟',
        'option1': 'لوکزامبورگ',
        'option2': 'اش-سور-آلزت',
        'option3': 'دیکیرش',
        'option4': 'اترناخ',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'کبوتر',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Rg چیست؟',
        'option1': 'رونتگنیم',
        'option2': 'رادیم',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز کوبه‌ای است؟',
        'option1': 'بانگو',
        'option2': 'پیانو',
        'option3': 'گیتار',
        'option4': 'فلوت',
        'correct_option': 1
    },
    {
        'text': 'چه کسی کتاب "اولیس" را نوشت؟',
        'option1': 'جیمز جویس',
        'option2': 'ویرجینیا وولف',
        'option3': 'دی اچ لارنس',
        'option4': 'ساموئل بکت',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اقیانوسیه است؟',
        'option1': 'ساموآ',
        'option2': 'ژاپن',
        'option3': 'فیلیپین',
        'option4': 'اندونزی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Cn چیست؟',
        'option1': 'کوپرنیسیم',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش المپیکی است؟',
        'option1': 'پرش با اسکی',
        'option2': 'شطرنج',
        'option3': 'بیلیارد',
        'option4': 'کریکت',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور موناکو کدام شهر است؟',
        'option1': 'موناکو',
        'option2': 'مونت کارلو',
        'option3': 'لا کوندامین',
        'option4': 'فونتوی',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'نهنگ عنبر',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Nh چیست؟',
        'option1': 'نیهونیم',
        'option2': 'نیکل',
        'option3': 'نئون',
        'option4': 'ناتریوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'گرانج',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "آبشار" را ساخت؟',
        'option1': 'ژان سیبلیوس',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'نپال',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Fl چیست؟',
        'option1': 'فلروویوم',
        'option2': 'فلورین',
        'option3': 'فاسفور',
        'option4': 'فریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'ووشو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور سان مارینو کدام شهر است؟',
        'option1': 'سان مارینو',
        'option2': 'بورگو ماگیوره',
        'option3': 'سراواله',
        'option4': 'فائتانو',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'مورچه پرنده',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Mc چیست؟',
        'option1': 'مسکوویوم',
        'option2': 'منگنز',
        'option3': 'مولیبدن',
        'option4': 'مس',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'کمانچه',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "سه نوازنده" را نقاشی کرد؟',
        'option1': 'پابلو پیکاسو',
        'option2': 'ژرژ براک',
        'option3': 'خوان گریس',
        'option4': 'فرناند لژه',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'لیختن اشتاین',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Lv چیست؟',
        'option1': 'لیورموریوم',
        'option2': 'لوتتیم',
        'option3': 'لیتیم',
        'option4': 'سرب',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'بازی های بومی',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور آندورا کدام شهر است؟',
        'option1': 'آندورا لا ولا',
        'option2': 'لس اسکالدز',
        'option3': 'انکمپ',
        'option4': 'سانت جولیا د لوریا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'شغال',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ts چیست؟',
        'option1': 'تننسین',
        'option2': 'تیتانیوم',
        'option3': 'تالیم',
        'option4': 'تلوریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'سینثپاپ',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "کارمینا بورانا" را ساخت؟',
        'option1': 'کارل اورف',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'اتیوپی',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Og چیست؟',
        'option1': 'اوگانسون',
        'option2': 'اکسیژن',
        'option3': 'اسمیم',
        'option4': 'اروپیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'راکتبال',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور واتیکان کدام شهر است؟',
        'option1': 'شهر واتیکان',
        'option2': 'رم',
        'option3': 'میلان',
        'option4': 'ونیز',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'هدهد',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد He چیست؟',
        'option1': 'هلیوم',
        'option2': 'هیدروژن',
        'option3': 'هافنیم',
        'option4': 'هولمیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'ویولن',
        'option2': 'پیکولو',
        'option3': 'گیتار',
        'option4': 'پیانو',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "خانواده تیبو" را نوشت؟',
        'option1': 'روژه مارتن دو گار',
        'option2': 'آندره مالرو',
        'option3': 'آلبر کامو',
        'option4': 'ژان پل سارتر',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای شمالی است؟',
        'option1': 'پاناما',
        'option2': 'برزیل',
        'option3': 'آرژانتین',
        'option4': 'شیلی',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Ne چیست؟',
        'option1': 'نئون',
        'option2': 'نیکل',
        'option3': 'ناتریوم',
        'option4': 'نیوبیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'قایقرانی کانو',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'تنیس',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور السالوادور کدام شهر است؟',
        'option1': 'سان سالوادور',
        'option2': 'سانتا آنا',
        'option3': 'سان میگل',
        'option4': 'سونسوناته',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'نهنگ قاتل',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ar چیست؟',
        'option1': 'آرگون',
        'option2': 'آرسنیک',
        'option3': 'آنتیموان',
        'option4': 'آلومینیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'آر اند بی',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "دانوب آبی" را ساخت؟',
        'option1': 'یوهان اشتراوس پسر',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'بوتان',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Kr چیست؟',
        'option1': 'کریپتون',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'سامبو',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور هندوراس کدام شهر است؟',
        'option1': 'تگوسیگالپا',
        'option2': 'سان پدرو سولا',
        'option3': 'لا سیبا',
        'option4': 'ال پروگرسو',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'سوسک چوب',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Xe چیست؟',
        'option1': 'زنون',
        'option2': 'زیرکونیوم',
        'option3': 'روی',
        'option4': 'ایریدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'رباب',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "دختران آوینیون" را نقاشی کرد؟',
        'option1': 'پابلو پیکاسو',
        'option2': 'آنری ماتیس',
        'option3': 'ژرژ روئو',
        'option4': 'آندره دورن',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'مولداوی',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Rn چیست؟',
        'option1': 'رادون',
        'option2': 'رادیم',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'بازی های سنتی',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور نیکاراگوئه کدام شهر است؟',
        'option1': 'ماناگوئه',
        'option2': 'لئون',
        'option3': 'گرانادا',
        'option4': 'ماسایا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'گرگ',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Fr چیست؟',
        'option1': 'فرانسیوم',
        'option2': 'فلورین',
        'option3': 'فاسفور',
        'option4': 'فریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'فولک',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "شهر طلایی" را ساخت؟',
        'option1': 'آنتون بروکنر',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'سومالی',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Ra چیست؟',
        'option1': 'رادیم',
        'option2': 'رادون',
        'option3': 'روتنیوم',
        'option4': 'روبیدیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'پدل',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور کاستاریکا کدام شهر است؟',
        'option1': 'سان خوزه',
        'option2': 'لیمون',
        'option3': 'سانتو دومینگو',
        'option4': 'آلاخوئلا',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پرنده است؟',
        'option1': 'خفاش',
        'option2': 'مرغ مگس',
        'option3': 'پروانه',
        'option4': 'مورچه',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Ac چیست؟',
        'option1': 'آکتینیم',
        'option2': 'آرسنیک',
        'option3': 'آنتیموان',
        'option4': 'آلومینیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز بادی است؟',
        'option1': 'ویولن',
        'option2': 'کورنت',
        'option3': 'گیتار',
        'option4': 'پیانو',
        'correct_option': 2
    },
    {
        'text': 'چه کسی کتاب "خشم و هیاهو" را نوشت؟',
        'option1': 'ویلیام فاکنر',
        'option2': 'ارنست همینگوی',
        'option3': 'اف اسکات فیتزجرالد',
        'option4': 'جان اشتاین بک',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آمریکای جنوبی است؟',
        'option1': 'پاراگوئه',
        'option2': 'کاستاریکا',
        'option3': 'پاناما',
        'option4': 'گواتمالا',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Th چیست؟',
        'option1': 'توریم',
        'option2': 'تیتانیوم',
        'option3': 'تالیم',
        'option4': 'تلوریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش آبی است؟',
        'option1': 'شنا با ماسک و لوله',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'تنیس',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور پاناما کدام شهر است؟',
        'option1': 'پاناما سیتی',
        'option2': 'کلون',
        'option3': 'داوید',
        'option4': 'سانتیاگو',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار دریایی است؟',
        'option1': 'کوسه',
        'option2': 'نهنگ گوژپشت',
        'option3': 'مارماهی',
        'option4': 'اختاپوس',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Pa چیست؟',
        'option1': 'پروتاکتینیم',
        'option2': 'پالادیم',
        'option3': 'پلاتین',
        'option4': 'پتاسیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'گاسپل',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "شوالیه رز" را ساخت؟',
        'option1': 'ریشارد اشتراوس',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آسیایی است؟',
        'option1': 'یمن',
        'option2': 'کنیا',
        'option3': 'مراکش',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Np چیست؟',
        'option1': 'نپتونیوم',
        'option2': 'نیکل',
        'option3': 'نئون',
        'option4': 'ناتریوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش رزمی است؟',
        'option1': 'کشتی',
        'option2': 'اسکی',
        'option3': 'شنا',
        'option4': 'دوچرخه سواری',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور جامائیکا کدام شهر است؟',
        'option1': 'کینگستون',
        'option2': 'مونته‌گو بی',
        'option3': 'اسپنیش تاون',
        'option4': 'پورت آنتونیو',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع حشره است؟',
        'option1': 'عنکبوت',
        'option2': 'مگس خانگی',
        'option3': 'عقرب',
        'option4': 'هزارپا',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Pu چیست؟',
        'option1': 'پلوتونیوم',
        'option2': 'پالادیم',
        'option3': 'پلاتین',
        'option4': 'پتاسیم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ساز زهی است؟',
        'option1': 'ترومپت',
        'option2': 'سه تار',
        'option3': 'فلوت',
        'option4': 'درام',
        'correct_option': 2
    },
    {
        'text': 'چه کسی تابلوی "شام در اموس" را نقاشی کرد؟',
        'option1': 'رامبرانت',
        'option2': 'کاراواجو',
        'option3': 'تیسین',
        'option4': 'ورمر',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها یک کشور اروپایی است؟',
        'option1': 'بلاروس',
        'option2': 'الجزایر',
        'option3': 'لیبی',
        'option4': 'مصر',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Am چیست؟',
        'option1': 'امریسیم',
        'option2': 'آنتیموان',
        'option3': 'آرسنیک',
        'option4': 'استرانسیوم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با توپ است؟',
        'option1': 'بازی های محلی',
        'option2': 'شنا',
        'option3': 'دوچرخه سواری',
        'option4': 'اسکی',
        'correct_option': 1
    },
    {
        'text': 'پایتخت کشور هائیتی کدام شهر است؟',
        'option1': 'پورت او پرنس',
        'option2': 'کاپ-آیتین',
        'option3': 'گونایوز',
        'option4': 'سن-مارک',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک نوع پستاندار است؟',
        'option1': 'مار',
        'option2': 'شیر',
        'option3': 'قورباغه',
        'option4': 'ماهی',
        'correct_option': 2
    },
    {
        'text': 'عنصر شیمیایی با نماد Cm چیست؟',
        'option1': 'کوریم',
        'option2': 'کربن',
        'option3': 'کبالت',
        'option4': 'کروم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک سبک موسیقی است؟',
        'option1': 'راکابیلی',
        'option2': 'رئالیسم',
        'option3': 'کوبیسم',
        'option4': 'باروک',
        'correct_option': 1
    },
    {
        'text': 'چه کسی سمفونی "پرواز زنبور عسل" را ساخت؟',
        'option1': 'نیکلای ریمسکی-کورساکف',
        'option2': 'یوهان سباستیان باخ',
        'option3': 'ولفگانگ آمادئوس موتزارت',
        'option4': 'لودویگ فان بتهوون',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک کشور آفریقایی است؟',
        'option1': 'اریتره',
        'option2': 'پرو',
        'option3': 'ویتنام',
        'option4': 'فیلیپین',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد Bk چیست؟',
        'option1': 'برکلیم',
        'option2': 'بور',
        'option3': 'بیسموت',
        'option4': 'باریم',
        'correct_option': 1
    },
    {
        'text': 'کدام یک از این‌ها یک ورزش با راکت است؟',
        'option1': 'پدل تنیس',
        'option2': 'فوتبال',
        'option3': 'بسکتبال',
        'option4': 'والیبال',
        'correct_option': 1
    },
    {
        'text': 'پایتخت ایران کدام شهر است؟',
        'option1': 'تهران',
        'option2': 'مشهد', 
        'option3': 'اصفهان',
        'option4': 'شیراز',
        'correct_option': 1
    },
    {
        'text': 'بلندترین کوه جهان کدام است؟',
        'option1': 'K2',
        'option2': 'مون بلان',
        'option3': 'اورست',
        'option4': 'البرز',
        'correct_option': 3
    },
    {
        'text': 'کدام سیاره به ستاره سرخ معروف است؟',
        'option1': 'زهره',
        'option2': 'مریخ',
        'option3': 'مشتری',
        'option4': 'زحل',
        'correct_option': 2
    },
    {
        'text': 'زبان برنامه نویسی پایتون در کدام کشور ایجاد شد؟',
        'option1': 'آمریکا',
        'option2': 'هلند',
        'option3': 'انگلیس',
        'option4': 'کانادا',
        'correct_option': 2
    },
    {
        'text': 'کدام حیوان بزرگ‌ترین حیوان خشکی است؟',
        'option1': 'فیل',
        'option2': 'زرافه',
        'option3': 'کرگدن',
        'option4': 'اسب آبی',
        'correct_option': 1
    },
    {
        'text': 'سالانه چند فصل دارد؟',
        'option1': '2',
        'option2': '3',
        'option3': '4',
        'option4': '5',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این‌ها یک سیاره کوتوله است؟',
        'option1': 'مریخ',
        'option2': 'پلوتو',
        'option3': 'زهره',
        'option4': 'اورانوس',
        'correct_option': 2
    },
    {
        'text': 'رنگ آسمان در روز آبی است به دلیل:',
        'option1': 'انعکاس نور از اقیانوس',
        'option2': 'پراکندگی رایلی',
        'option3': 'وجود اکسیژن',
        'option4': 'نور خورشید',
        'correct_option': 2
    },
    {
        'text': 'کدام یک از این‌ها پایتخت ژاپن است؟',
        'option1': 'توکیو',
        'option2': 'سئول',
        'option3': 'پکن',
        'option4': 'بانکوک',
        'correct_option': 1
    },
    {
        'text': 'عنصر شیمیایی با نماد O چیست؟',
        'option1': 'طلا',
        'option2': 'اکسیژن',
        'option3': 'اسمیم',
        'option4': 'اسمانتیم',
        'correct_option': 2
    },
        {
        'text': 'کدام عنصر شیمیایی با نماد O نشان داده می‌شود؟',
        'option1': 'طلا',
        'option2': 'اکسیژن',
        'option3': 'اسمیم',
        'option4': 'اسمانتیم',
        'correct_option': 2
    },
    {
        'text': 'پایتخت کشور مصر چیست؟',
        'option1': 'اسکندریه',
        'option2': 'قاهره',
        'option3': 'جیزه',
        'option4': 'سوئز',
        'correct_option': 2
    },
    {
        'text': 'کدام جنگ در سال 1945 به پایان رسید؟',
        'option1': 'جنگ جهانی اول',
        'option2': 'جنگ ویتنام',
        'option3': 'جنگ جهانی دوم',
        'option4': 'جنگ کره',
        'correct_option': 3
    },
    {
        'text': 'کدام یک از این آثار متعلق به سعدی است؟',
        'option1': 'شاهنامه',
        'option2': 'مثنوی معنوی',
        'option3': 'دیوان حافظ',
        'option4': 'گلستان',
        'correct_option': 4
    },
    {
        'text': 'جذر عدد 64 چیست؟',
        'option1': '6',
        'option2': '7',
        'option3': '8',
        'option4': '9',
        'correct_option': 3
    },
    {
        'text': 'کدام کشور میزبان المپیک 2012 بود؟',
        'option1': 'چین',
        'option2': 'یونان',
        'option3': 'برزیل',
        'option4': 'انگلستان',
        'correct_option': 4
    },
    {
        'text': 'کدام نقاش تابلوی "شام آخر" را خلق کرد؟',
        'option1': 'میکل آنژ',
        'option2': 'رامبرانت',
        'option3': 'لئوناردو داوینچی',
        'option4': 'ون گوگ',
        'correct_option': 3
    },
    {
        'text': 'کدام شرکت آیفون را تولید می‌کند؟',
        'option1': 'سامسونگ',
        'option2': 'گوگل',
        'option3': 'اپل',
        'option4': 'هواوی',
        'correct_option': 3
    },
    {
        'text': 'کدام جانور در دسته خزندگان قرار می‌گیرد؟',
        'option1': 'قورباغه',
        'option2': 'مار',
        'option3': 'پنگوئن',
        'option4': 'دلفین',
        'correct_option': 2
    },
    {
        'text': 'بزرگترین سیاره در منظومه شمسی کدام است؟',
        'option1': 'زمین',
        'option2': 'مریخ',
        'option3': 'مشتری',
        'option4': 'زحل',
        'correct_option': 3
    }
]













print("در حال اضافه کردن سوالات...")

for i, q_data in enumerate(questions, 1):
    question, created = Question.objects.get_or_create(
        text=q_data['text'],
        defaults={
            'option1': q_data['option1'],
            'option2': q_data['option2'],
            'option3': q_data['option3'],
            'option4': q_data['option4'],
            'correct_option': q_data['correct_option']
        }
    )
    if created:
        print(f'✅ {i}. سوال اضافه شد: {question.text[:40]}...')
    else:
        print(f'⚠️ {i}. سوال از قبل وجود داشت: {question.text[:40]}...')

print(f"\n🎉 تعداد سوالات در دیتابیس: {Question.objects.count()}")