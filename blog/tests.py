from django.test import TestCase

from django.contrib.auth.models import User

from .models import Category, Post


class Test_Create_Post(TestCase):


    @classmethod
    def setUpTestData(cls) -> None:
        
        test_user1 = User.objects.create_user(
            username='test_user1',
            password='password'
        )

        test_category = Category.objects.create(name='django')
        test_post1 = Post.objects.create(
            category_id=1,
            title='Post Title',
            excerpt='Post Excerpt',
            content='Post Content',
            status='published',
            slug='post-title',
            author_id=1
        )

    
    def test_blog_content(self):
        
        post = Post.objects.get(id=1)
        category = Category.objects.get(id=1)

        author = f'{post.author}'
        title = f'{post.title}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')

        # self.author + '- ' + self.title
        self.assertEqual(str(post), 'test_user1- Post Title')
        # self.name
        self.assertEqual(str(category), 'django')
