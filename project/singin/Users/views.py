from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Question, UserAnswer, QuizSettings
from .forms import CustomUserCreationForm, LoginForm
import random

def home(request):
    """صفحه اصلی - فقط ثبت نام و ورود"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'Users/home.html')

def register_view(request):
    """صفحه ثبت نام"""
    if request.user.is_authenticated:
        messages.info(request, 'شما قبلاً وارد سیستم شده‌اید!')
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'👋 {user.username} عزیز، خوش آمدید!')
            return redirect('dashboard')
        else:
            messages.error(request, 'لطفاً خطاهای زیر را اصلاح کنید:')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'Users/register.html', {'form': form})

def login_view(request):
    """صفحه ورود"""
    if request.user.is_authenticated:
        messages.info(request, 'شما قبلاً وارد سیستم شده‌اید!')
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'🎉 {username} عزیز، خوش آمدید!')
                return redirect('dashboard')
            else:
                messages.error(request, '❌ نام کاربری یا رمز عبور اشتباه است')
    else:
        form = LoginForm()
    
    return render(request, 'Users/login.html', {'form': form})

@login_required
def dashboard(request):
    """پنل کاربری شخصی - فقط برای کاربران لاگین شده"""
    user = request.user
    
    # گرفتن 100 کاربر برتر
    top_users_query = CustomUser.objects.all().order_by('-total_score')
    top_users = list(top_users_query[:100])
    
    # پیدا کردن رتبه کاربر
    user_rank = user.get_rank()
    
    # بررسی اینکه آیا کاربر در لیست 100 نفر برتر هست (روش درست)
    user_in_top_100 = any(top_user.id == user.id for top_user in top_users)
    
    can_take_quiz, quiz_message = user.can_take_quiz()
    
    context = {
        'user': user,
        'can_take_quiz': can_take_quiz,
        'quiz_message': quiz_message,
        'top_users': top_users,
        'user_rank': user_rank,
        'user_in_top_100': user_in_top_100,
    }
    return render(request, 'Users/dashboard.html', context)

@login_required
def quiz_view(request):
    """صفحه آزمون - فقط برای کاربران لاگین شده"""
    user = request.user
    
    # بررسی قلب‌ها
    can_take_quiz, message = user.can_take_quiz()
    if not can_take_quiz:
        messages.warning(request, message)
        return redirect('dashboard')
    
    # گرفتن تنظیمات
    quiz_settings = QuizSettings.objects.first()
    if not quiz_settings:
        quiz_settings = QuizSettings.objects.create()
    
    # گرفتن سوالات
    answered_questions = UserAnswer.objects.filter(user=user).values_list('question_id', flat=True)
    available_questions = Question.objects.exclude(id__in=answered_questions)
    
    if available_questions.count() < quiz_settings.total_questions:
        available_questions = Question.objects.all().order_by('used_count')
    
    questions = list(available_questions[:quiz_settings.total_questions])
    random.shuffle(questions)
    
    if not questions:
        messages.error(request, 'در حال حاضر سوالی برای نمایش وجود ندارد')
        return redirect('dashboard')
    
    if request.method == 'POST':
        score = 0
        answered_count = 0
        
        for question in questions:
            field_name = f'question_{question.id}'
            if field_name in request.POST:
                answered_count += 1
                selected_option = int(request.POST[field_name])
                is_correct = selected_option == question.correct_option
                
                UserAnswer.objects.create(
                    user=user,
                    question=question,
                    selected_option=selected_option,
                    is_correct=is_correct
                )
                
                question.used_count += 1
                question.save()
                
                if is_correct:
                    score += quiz_settings.points_per_correct
                else:
                    score += quiz_settings.points_per_wrong
        
        # کاهش قلب بعد از اتمام آزمون
        user.hearts -= 1
        user.total_score += score
        user.save()
        
        # پیام نتیجه
        if score > 0:
            messages.success(request, f'آفرین! شما {score} امتیاز کسب کردید')
        else:
            messages.info(request, f'امتیاز شما: {score}. دفعه بعدی بهتر عمل کنید!')
        
        return redirect('dashboard')
    
    context = {
        'questions': questions,
        'quiz_settings': quiz_settings,
        'user': user,
    }
    return render(request, 'Users/quiz.html', context)

@login_required
def buy_heart(request):
    """خرید قلب"""
    user = request.user
    success, message = user.buy_heart()
    
    if success:
        messages.success(request, message)
    else:
        messages.warning(request, message)
    
    return redirect('dashboard')

@login_required
def leaderboard(request):
    """صفحه رتبه‌بندی (فقط 100 نفر برتر)"""
    top_users_query = CustomUser.objects.all().order_by('-total_score')
    top_users = list(top_users_query[:100])
    user_rank = request.user.get_rank()
    user_in_top_100 = any(top_user.id == request.user.id for top_user in top_users)
    
    context = {
        'top_users': top_users,
        'user_rank': user_rank,
        'user_in_top_100': user_in_top_100,
    }
    return render(request, 'Users/leaderboard.html', context)

def logout_view(request):
    """خروج از سیستم"""
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید')
    return redirect('home')