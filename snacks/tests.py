from django.test import TestCase
from django.urls import reverse

class SnacksTest(TestCase):
    def test_snack_list_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_snack_list_template(self):
        response = self.client.get(reverse('snack_list'))
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_detail_status_code(self):
        response = self.client.get(reverse('snack_detail', args=[1]))
        self.assertEquals(response.status_code, 200)
    
    def test_detail_template(self):
        response = self.client.get(reverse('snack_detail', args=[1]))
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_create_status_code(self):
        response = self.client.post('/create/', {'title': 'Snack', 'description': 'A snack', 'purchaser':'admin'})
        self.assertEquals(response.status_code, 200)
    
    def test_create_template(self):
        response = self.client.post('/create/', {'title': 'Snack', 'description': 'A snack', 'purchaser':'admin'})
        self.assertTemplateUsed(response, 'snack_new.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_update_status_code(self):
        response = self.client.post('/1/update/', {'title': 'Snack', 'description': 'A snack'})
        self.assertEquals(response.status_code, 200)

    def test_update_template(self):
        response = self.client.post('/1/update/', {'title': 'Snack', 'description': 'A snack'})
        self.assertTemplateUsed(response, 'snack_edit.html')
        self.assertTemplateUsed(response, '_base.html')
    
    def test_delete_status_code(self):
        response = self.client.get(reverse('snack_delete', args=[1]))
        self.assertEquals(response.status_code, 204)

    def test_delete_template(self):
        response = self.client.get(reverse('snack_delete', args=[1]))
        self.assertTemplateUsed(response, 'snack_delete.html')
        self.assertTemplateUsed(response, '_base.html')
