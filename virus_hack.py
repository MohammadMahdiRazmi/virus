
    # مسیری که می‌خواهید فایل‌ها در آن ایجاد شوند
directory = "virus"

# ایجاد دایرکتوری اگر وجود نداشته باشد


    # تعداد فایل‌های مورد نیاز
num_files = 100

    # متنی که می‌خواهیم در فایل‌ها بنویسیم
message = "You have been hacked"

for i in range(1, num_files + 1):
        # نام فایل
    filename = f"{directory}/file_{i}.txt"

        # باز کردن فایل برای نوشتن
    a = open(filename, 'w')
    a.write(message)

