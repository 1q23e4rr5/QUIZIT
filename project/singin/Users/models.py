from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta

class CustomUser(AbstractUser):
    hearts = models.IntegerField(default=5)
    hearts_last_update = models.DateTimeField(default=timezone.now)
    total_score = models.IntegerField(default=0)
    
    def can_take_quiz(self):
        if self.hearts > 0:
            return True, "می‌توانید آزمون دهید"
        else:
            time_since_update = timezone.now() - self.hearts_last_update
            # اصلاح خطا: استفاده از = به جای ==
            if time_since_update >= timedelta(minutes=1):  # این خط اصلاح شد
                self.hearts = 5
                self.hearts_last_update = timezone.now()
                self.save()
                return True, "قلب‌های شما شارژ شد!"
            else:
                remaining = timedelta(minutes=1) - time_since_update
                total_seconds = int(remaining.total_seconds())
                minutes = total_seconds // 60
                seconds = total_seconds % 60
                return False, f"{minutes:02d}:{seconds:02d} تا دریافت قلب رایگان"
    
    def buy_heart(self):
        if self.total_score >= 70:
            self.total_score -= 70
            self.hearts += 5
            self.save()
            return True, "قلب با موفقیت خریداری شد"
        return False, "امتیاز کافی ندارید (حداقل 70 امتیاز نیاز است)"
    
    def get_rank(self):
        """محاسبه رتبه کاربر"""
        users_above = CustomUser.objects.filter(total_score__gt=self.total_score).count()
        return users_above + 1

class QuizSettings(models.Model):
    total_questions = models.IntegerField(default=10)
    points_per_correct = models.IntegerField(default=1)
    points_per_wrong = models.IntegerField(default=-1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return "تنظیمات آزمون"

class Question(models.Model):
    text = models.TextField(verbose_name="متن سوال")
    option1 = models.CharField(max_length=200, verbose_name="گزینه ۱")
    option2 = models.CharField(max_length=200, verbose_name="گزینه ۲")
    option3 = models.CharField(max_length=200, verbose_name="گزینه ۳")
    option4 = models.CharField(max_length=200, verbose_name="گزینه ۴")
    correct_option = models.IntegerField(
        choices=[(1, 'گزینه ۱'), (2, 'گزینه ۲'), (3, 'گزینه ۳'), (4, 'گزینه ۴')],
        verbose_name="گزینه صحیح"
    )
    used_count = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:50]

class UserAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="کاربر")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="سوال")
    selected_option = models.IntegerField(
        choices=[(1, 'گزینه ۱'), (2, 'گزینه ۲'), (3, 'گزینه ۳'), (4, 'گزینه ۴')],
        verbose_name="گزینه انتخاب شده"
    )
    is_correct = models.BooleanField(default=False, verbose_name="صحیح/غلط")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "پاسخ کاربر"
        verbose_name_plural = "پاسخ‌های کاربران"