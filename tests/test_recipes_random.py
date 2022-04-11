from common import SpoonacularTests


class TestRecipesRandom(SpoonacularTests):
    
    def test_recipes_random(self):

        base_url, request_parameters = self.get_reques_data(__name__)
        random_recipe_request_url = self.get_request_url(base_url, request_parameters)

        random_recipe_reply = self.get_reply(random_recipe_request_url)

        assert random_recipe_reply.status_code == 200
        json_random_recipe_reply = random_recipe_reply.json()
        assert 'id' in json_random_recipe_reply.get('recipes')[0]
        tags = request_parameters['tags'].split(',')
        for tag in tags:
            assert json_random_recipe_reply.get('recipes')[0][tag] == True
