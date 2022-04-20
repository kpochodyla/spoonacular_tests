from utils import SpoonacularTests


class TestRecipesAutocomplete(SpoonacularTests):
    
    def test_recipes_autocomplete(self):
        base_url, request_parameters = self.get_request_data("test_recipes_autocomplete")
        recipe_autocomplete_request_url = self.get_request_url(base_url, request_parameters)
        recipe_autocomplete_reply = self.get_request(recipe_autocomplete_request_url)

        assert recipe_autocomplete_reply.status_code == 200
        json_recipe_autocomplete_reply = recipe_autocomplete_reply.json()
        for recipe in json_recipe_autocomplete_reply:
            assert 'wrap' in recipe.get('title')
