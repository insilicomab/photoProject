from django.urls import path
from .views import IndexView, CreatePhotoView, PostSuccessView, CategoryView, UserView, DetailView, MypageView, PhotoDeleteView

app_name = 'photo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/', CreatePhotoView.as_view(), name='post'),
    path('post_done/', PostSuccessView.as_view(), name='post_done'),

    # カテゴリ一覧ページ
    # photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>', CategoryView.as_view(), name = 'photos_cat'),

    # ユーザーの投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>', UserView.as_view(), name = 'user_list'),

    # 詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo-detail/<int:pk>', DetailView.as_view(), name = 'photo_detail'),

    path('mypage/', MypageView.as_view(), name = 'mypage'),

    # 投稿写真の削除
    # photo/<Photo postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name = 'photo_delete'),

]