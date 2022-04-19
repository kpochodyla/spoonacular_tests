from common import SpoonacularTests


class TestRecipesInformation(SpoonacularTests):
    
    def test_recipes_information(self):
        base_url, request_parameters = self.get_request_data("test_recipes_information")
        recipe_information_request_url = self.insert_request_params(base_url, request_parameters)
        recipe_information_reply = self.get_reply(recipe_information_request_url)

        assert recipe_information_reply.status_code == 200
        json_recipe_information_reply = recipe_information_reply.json()
        assert json_recipe_information_reply.get('id') == request_parameters['id']

    def test_recipes_information_bad_request(self):
        base_url, request_parameters = self.get_request_data("test_recipes_information_bad_request")
        recipe_information_bad_request_url = self.insert_request_params(base_url, request_parameters)
        recipe_information_bad_request_reply = self.get_reply(recipe_information_bad_request_url)
        assert recipe_information_bad_request_reply.status_code == 404
