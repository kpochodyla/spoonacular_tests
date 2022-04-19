from common import SpoonacularTests


class TestRecipesInstrtuctions(SpoonacularTests):
    
    def test_recipes_instructions(self):
        base_url, request_parameters = self.get_request_data("test_recipes_get_instructions")
        recipe_instructions_request_url = self.insert_request_params(base_url, request_parameters)
        recipe_instructions_reply = self.get_reply(recipe_instructions_request_url)

        assert recipe_instructions_reply.status_code == 200
        json_recipe_instructions_reply = recipe_instructions_reply.json()
        assert 'steps' in json_recipe_instructions_reply[0]
        assert len(json_recipe_instructions_reply[0]['steps']) > 0
