from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import Post, Category


class PostTest(APITestCase):
    

    def test_view_post(self):

        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_create_post(self):
        
        self.test_user1 = User.objects.create_user(
            username='test_user1',
            password='password' 
        )

        self.test_category = Category.objects.create(name='django')

        self.client.login(
            username=self.test_user1.username,
            password='password')

        data = {
            'author': 1,
            'title': 'Post Title',
            'excerpt': 'Post Excerpt',
            'content': 'Post Content',
        }

        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response_body = response.json()
        
        self.assertEqual(response_body['author'], 1)
        self.assertEqual(response_body['title'], 'Post Title')
        self.assertEqual(response_body['excerpt'], 'Post Excerpt')
        self.assertEqual(response_body['content'], 'Post Content')


    def test_update_post(self):

        self.test_user1 = User.objects.create_user(
            username='test_user1',
            password='password' 
        )

        post_create_data = {
            'author': self.test_user1,
            'title': 'Post Title',
            'excerpt': 'Post Excerpt',
            'content': 'Post Content',
        }

        self.test_post = Post.objects.create(**post_create_data)
        self.test_category = Category.objects.create(name='django')

        self.client.login(
            username=self.test_user1.username,
            password='password')
        
        post_update_data1 = {
            'author': 1,
            'title': 'Post Title Updated 1',
            'excerpt': 'Post Excerpt Updated 1',
            'content': 'Post Content Updated 1',
        }

        url = reverse(('blog_api:detailupdatedelete'), kwargs={'pk': 1})
        response = self.client.put(url, post_update_data1, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_body = response.json()

        self.assertEqual(response_body['author'], 1)
        self.assertEqual(response_body['title'], 'Post Title Updated 1')
        self.assertEqual(response_body['excerpt'], 'Post Excerpt Updated 1')
        self.assertEqual(response_body['content'], 'Post Content Updated 1')

        # not allowed test

        self.test_user2 = User.objects.create_user(
            username = 'test_user2',
            password = 'password'
        )

        self.client.login(
            username=self.test_user2.username,
            password='password')

        post_update_data2 = {
            'author': 2,
            'title': 'Post Title Updated 2',
            'excerpt': 'Post Excerpt Updated 2',
            'content': 'Post Content Updated 2',
        }

        response = self.client.put(url, post_update_data2, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)