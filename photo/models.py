from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    
    def __str__(self):
        return self.title

class PhotoPost(models.Model):
    '''モデルクラス
    CustomUserモデル(のuser_id)とPhotoPostモデルを1対多の関係で結び付ける
    CustomUserが親でPhotoPostが子の関係となる
    '''
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        )
    '''
    Categoryモデル(のtitle)とPhotoPostモデルを1対多の関係で結び付ける
    Categoryが親でPhotoPostが子の関係となる
    '''
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT # カテゴリに関連付けられた投稿データが存在する場合はそのカテゴリを削除できないようにする
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200        # 最大文字数は200
        )
    # コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント',
        )
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to = 'photos'   # MEDIA_ROOT以下のphotosにファイルを保存  
        )
    # イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to = 'photos',  # MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,            # フィールド値の設定は必須でない
        null=True              # データベースにnullが保存されることを許容
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True      # 日時を自動追加
        )
    
    def __str__(self):
        return self.title