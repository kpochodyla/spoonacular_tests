from utils import SpoonacularTests


class TestRecipesExtract(SpoonacularTests):
    
    def test_recipes_extract(self):
        base_url, request_parameters = self.get_request_data("test_recipes_extract")
        recipe_extract_request_url = self.get_request_url(base_url, request_parameters)
        recipe_extract_reply = self.get_request(recipe_extract_request_url)

        assert recipe_extract_reply.status_code == 200
        json_recipe_extract_reply = recipe_extract_reply.json()
        assert 'analyzedInstructions' in json_recipe_extract_reply
        assert len(json_recipe_extract_reply.get('analyzedInstructions')) > 0
        assert json_recipe_extract_reply.get('title')== 'Ugly Cake'
        taste = json_recipe_extract_reply.get('taste')
        assert 'sweetness' in taste
        assert 'saltiness' in taste
        assert 'sourness' in taste
        assert 'bitterness' in taste
        assert 'savoriness' in taste
        assert 'fattiness' in taste
        assert 'spiciness' in taste
