import os
from kivy.app import App
from kivy.uix.browser import WebView # لضمان عمل المتصفح الداخلي
from kivy.core.window import Window

class MyWebViewApp(App):
    def build(self):
        # هذا السطر يخبر التطبيق بفتح ملف index.html الموجود داخل مجلد www
        # سنستخدم الطريقة الأكثر استقراراً لـ Buildozer
        from android.runnable import run_on_ui_thread
        
        # كود بسيط لتشغيل واجهة الويب
        return None 

if __name__ == "__main__":
    # ملاحظة: أداة Buildozer ستقوم بدمج هذا مع مكتبة WebView تلقائياً
    # تأكد فقط أن ملفك الأساسي اسمه index.html داخل مجلد www
    pass

