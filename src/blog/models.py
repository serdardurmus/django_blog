from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"  # Datebase de görüntüsünü değiştirdik sadece
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),  # 1.si database kaydedilmesi, 2.si kullanıcıya gözükme şekli
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # Protect tablonun silinmesine izin vermiyr, eğer bunu iin verirsek (CASCADE ile) tm post gidiyor
    publish_date = models.DateTimeField(auto_now_add=True)  # save ettiğimizde otomatik olarak datebase tarih ve saati koyuyuor
    last_updated = models.DateTimeField(auto_now=True)  # her update edildiğinde Time ı değiştiriyor
    # ForeignKey: Bir postun bir kategorisi olacak ama bir kategorinin birden fazla postu olabilir)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)  # Blank zorunlu değil demek
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username