from utils import SpoonacularTests


class TestRecipesSimilar(SpoonacularTests):
    
    def test_recipes_similar(self):
        base_url, request_parameters = self.get_request_data("test_recipes_similar")
        recipe_similar_request_url = self.get_request_url(base_url, request_parameters)
        recipe_similar_reply = self.get_request(recipe_similar_request_url)

        assert recipe_similar_reply.status_code == 200
        json_recipe_similar_reply = recipe_similar_reply.json()
        assert len(json_recipe_similar_reply) > 0
        assert len(json_recipe_similar_reply) <= int(request_parameters['number'])
        for recipe in json_recipe_similar_reply:
            assert 'id' in recipe
            assert 'title' in recipe
