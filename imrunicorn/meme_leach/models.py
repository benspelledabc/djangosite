from django.db import models

# https://github.com/benspelledabc/Meme_Api
# {
#     "postLink": "https://redd.it/ji1riw",
#     "subreddit": "wholesomememes",
#     "title": "It makes me feel good.",
#     "url": "https://i.redd.it/xuzd77yl8bv51.png",
#     "nsfw": false,
#     "spoiler": false,
#     "author": "polyesterairpods",
#     "ups": 306,
#     "preview": [
#         "https://preview.redd.it/xuzd77yl8bv51.png?width=108&crop=smart&auto=webp&s=9a0376741fbda988ceeb7d96fdec3982f102313e",
#         "https://preview.redd.it/xuzd77yl8bv51.png?width=216&crop=smart&auto=webp&s=ee2f287bf3f215da9c1cd88c865692b91512476d",
#         "https://preview.redd.it/xuzd77yl8bv51.png?width=320&crop=smart&auto=webp&s=88850d9155d51f568fdb0ad527c94d556cd8bd70",
#         "https://preview.redd.it/xuzd77yl8bv51.png?width=640&crop=smart&auto=webp&s=b7418b023b2f09cdc189a55ff1c57d531028bc3e"
#         ]
# }


class LeachedMemePreview(models.Model):
    post_link = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s" % self.post_link

    class Meta:
        ordering = ('post_link', )
        verbose_name = 'Leached Meme Preview'
        verbose_name_plural = 'Leached Meme Previews'


class LeachedMeme(models.Model):
    post_link = models.CharField(max_length=250)
    subreddit = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250, unique=True)
    nsfw = models.BooleanField(default=False, null=True)
    spoiler = models.BooleanField(default=False, null=True)
    author = models.CharField(max_length=150)
    ups = models.IntegerField(default=1, null=True)
    # preview = models.ManyToManyField(LeachedMemePreview, blank=True)

    def __str__(self):
        return "[%s] - %s" % (self.subreddit, self.title)

    class Meta:
        ordering = ('subreddit', )
        verbose_name = 'Leached Meme'
        verbose_name_plural = 'Leached Memes'
