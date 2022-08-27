from rest_framework.test import APITestCase
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

        self.test_category = Category.objects.create(name='djangp')

        self.test_user1 = User.objects.create_user(
            username='test_user1',
            password='password' 
        )

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



