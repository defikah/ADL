class MethodProduct():
    def create_product(self):
        root_url = 'https://gorest.co.in'
        param_url = 'public-api/products'
        headers = {
            "Authorization" : "Bearer e3479c4068b18c10ce220f5665f1c206bff27b3e9a722bcc35cf52e36708a1fb"
        }

        name = "".join(random.choice(string.ascii_letters) for _ in range(8))
        description = "".join(random.choice(string.ascii_letters) for _ in range(20))
        message = ''.join(random.choice(string.ascii_letters) for _ in range(15))
        image = "www.google.com"
        price = 3000
        status = False

        body_json = dict(
            name=name,
            description=description,
            image=image,
            price=price,
            status=status
        )
        req_url = '{}/{}'.format(root_url, param_url)

        respon_url = requests.post(req_url, data=body_json, headers=headers)
        respon_trans = respon_url.json()

        return respon_trans

class TestStringMethods(unittest.TestCase):

    def test_success_create_product(self):

        respon = MethodProduct.create_product(self)

        self.assertEqual(respon['code'], 201)
        self.assertEqual(type(respon['data']['name']), type(str()))
        self.assertEqual(type(respon['data']['image']), type(str()))
        self.assertEqual(type(respon['data']['description']), type(str()))

    def test_detail_product(self):
        root_url = 'https://gorest.co.in'
        param_url = 'public-api/products'
        req_url = '{}/{}'.format(root_url, param_url)

        respon_post = MethodProduct.create_product(self)

        params_json = {'id':int(respon_post['data']['id'])}

        respon_url = requests.get(req_url, params=params_json)
        respon_get = respon_url.json()

        self.assertEqual(respon_post['data']['name'], respon_get['data'][0]['name'])
        self.assertEqual(respon_post['data']['image'], respon_get['data'][0]['image'])
        self.assertEqual(respon_post['data']['description'], respon_get['data'][0]['description'])

    def test_detail_product(self):
        root_url = 'https://gorest.co.in'
        param_url = 'public-api/products'
        req_url = '{}/{}'.format(root_url, param_url)

        respon_post = MethodProduct.create_product(self)

        params_json = {'id':int(respon_post['data']['id'])}

        respon_url = requests.get(req_url, params=params_json)
        respon_get = respon_url.json()

        self.assertEqual(respon_post['data']['name'], respon_get['data'][0]['name'])
        self.assertEqual(respon_post['data']['image'], respon_get['data'][0]['image'])
        self.assertEqual(respon_post['data']['description'], respon_get['data'][0]['description'])
