from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TownListTests(APITestCase):

    def setUp(self) -> None:
        pass

    def test_status(self):
        """Testing status code in answer"""

        url = reverse('town_list')
        response_get = self.client.get(url, format='json')
        response_post = self.client.post(url, format='json')

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class StreetListTests(APITestCase):

    def setUp(self) -> None:
        pass

    def test_status(self):
        """Testing status code in answer"""

        url = reverse('street_list', kwargs={'town_id': 10})
        response_get = self.client.get(url, format='json')
        response_post = self.client.post(url, format='json')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)



class ShopTests(APITestCase):

    def setUp(self) -> None:
        pass

    def test_status(self):
        """Testing status code in answer"""

        url = reverse('shop')
        response_get = self.client.get(url, format='json')
        response_post_200 = self.client.post(
            url,
            {
                "name": "achan__test",
                "town": "Боровск__test",
                "street": "Знатная",
                "house": "1",
                "opening_time": "08:00:00",
                "closing_time": "16:00:00"
            },
            format='json',
        )
        response_post_400 = self.client.post(
            url,
            {
                "name": "achan__test",
                "town": "Боровск__test",
                "street": "Знатная",
                "house": "1",
                "opening_time": "08:00ASD",
                "closing_time": "16:00:00"
            },
            format='json',
        )

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post_200.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_post_400.status_code, status.HTTP_400_BAD_REQUEST)