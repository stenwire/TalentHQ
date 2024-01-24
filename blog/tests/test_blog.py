# blog/tests.py
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from blog.models import BlogPost
from authme.models import CustomUser

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(email='testuser@mail.com', username='testuser', password='testpassword'):
        return CustomUser.objects.create_user(email=email, username=username, password=password)
    return _create_user

@pytest.fixture
def create_blog_post(create_user):
    def _create_blog_post(author=None, title='Test Post', content='This is a test post.'):
        if author is None:
            author = create_user()
        return BlogPost.objects.create(title=title, content=content, author=author)
    return _create_blog_post

@pytest.mark.django_db
class TestBlogPostAPI:
    def test_list_blog_posts(self, api_client, create_blog_post, create_user):
        user = create_user()
        blog_post = create_blog_post(author=user)
        response = api_client.get('/api/v1/blog/posts/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_retrieve_blog_post(self, api_client, create_blog_post, create_user):
        user = create_user()
        blog_post = create_blog_post(author=user)
        response = api_client.get(f'/api/v1/blog/posts/{blog_post.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Test Post'

    def test_create_blog_post(self, api_client, create_user):
        user = create_user()
        api_client.force_authenticate(user=user)
        data = {'title': 'New Post', 'content': 'This is a new post.'}
        response = api_client.post('/api/v1/blog/posts/', data)
        assert response.status_code == status.HTTP_201_CREATED
        assert BlogPost.objects.count() == 1

    def test_update_blog_post(self, api_client, create_blog_post, create_user):
        user = create_user()
        blog_post = create_blog_post(author=user)
        api_client.force_authenticate(user=user)
        data = {'title': 'Updated Post', 'content': 'This post has been updated.'}
        response = api_client.put(f'/api/v1/blog/posts/{blog_post.id}/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Updated Post'

    def test_delete_blog_post(self, api_client, create_blog_post, create_user):
        user = create_user()
        blog_post = create_blog_post(author=user)
        api_client.force_authenticate(user=user)
        response = api_client.delete(f'/api/v1/blog/posts/{blog_post.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert BlogPost.objects.count() == 0

    def test_unauthorized_create_blog_post(self, api_client):
        data = {'title': 'New Post', 'content': 'This is a new post.'}
        response = api_client.post('/api/v1/blog/posts/', data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
