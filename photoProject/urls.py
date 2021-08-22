from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings           # settingsを追加
from django.conf.urls.static import static # staticを追加

urlpatterns = [
    path('admin/', admin.site.urls),
    # photo.urlsへのURLパターンを追加
    path('', include('photo.urls')),
    # accounts.urlsへのURLパターンを追加
    path('', include('accounts.urls')),

    # パスワードリセット申し込みページ
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    # メール送信完了ページ
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    # パスワードリセットページ
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    # パスワードリセット完了ページ
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
]

# urlpatternsにmediaフォルダーのURLパターンを追加
urlpatterns += static(
  settings.MEDIA_URL,               # MEDIA_URL = '/media/'
  document_root=settings.MEDIA_ROOT # MEDIA_ROOTにリダイレクト
  )