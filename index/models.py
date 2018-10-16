from django.db import models

class User(models.Model):
    uphone = models.CharField(max_length=32)
    upwd = models.CharField(max_length=32)
    uname = models.CharField(max_length=16)
    uemail = models.EmailField(null=True)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.uname


class GoodsType(models.Model):
    title = models.CharField(max_length=40)
    picture = models.ImageField(upload_to=
        'static/upload/goodstype')
    desc = models.TextField()
    def __str__(self):
        return self.title
    def to_dict(self):
        dic = {
            'title':self.title,
            'picture':self.picture.__str__(),
            'desc':self.desc
        }
        return dic

class Goods(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    spec = models.CharField(max_length=20)
    picture = models.ImageField(upload_to=
        'static/upload/goodstype')
    isActive = models.BooleanField(default=True)
    goodstype = models.ForeignKey(GoodsType,null=True)
    def __str__(self):
        return self.title
