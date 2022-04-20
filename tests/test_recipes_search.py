from utils import SpoonacularTests


class TestRecipesSearch(SpoonacularTests):
    
    def test_recipes_search(self):
        base_url, request_parameters = self.get_request_data("test_recipes_search")
        recipe_search_request_url = self.get_request_url(base_url, request_parameters)
        recipe_search_reply = self.get_request(recipe_search_request_url)

        assert recipe_search_reply.status_code == 200
        json_recipe_search_reply = recipe_search_reply.json()
        assert len(json_recipe_search_reply.get('results')) > 0
        assert 'id' in json_recipe_search_reply.get('results')[0]
        assert 'nutrition' in json_recipe_search_reply.get('results')[0]


    def test_recipes_search_by_nutrients(self):
        base_url, request_parameters = self.get_request_data("test_recipes_search_by_nutrients")
        recipe_search_by_nutrients_request_url = self.get_request_url(base_url, request_parameters)
        recipe_search_by_nutrients_reply = self.get_request(recipe_search_by_nutrients_request_url)

        assert recipe_search_by_nutrients_reply.status_code == 200
        json_recipe_search_by_nutrients_reply = recipe_search_by_nutrients_reply.json()
        assert len(json_recipe_search_by_nutrients_reply) > 0
        assert 'id' in json_recipe_search_by_nutrients_reply[0]
        carbs = json_recipe_search_by_nutrients_reply[0].get('carbs')[:-1]
        sugar = json_recipe_search_by_nutrients_reply[0].get('sugar')[:-1]
        assert int(request_parameters['maxCarbs']) > int(carbs)
        assert int(request_parameters['minCarbs']) < int(carbs)
        assert int(request_parameters['maxSugar']) > int(sugar) 

    def test_recipes_search_by_ingredients(self):
        base_url, request_parameters = self.get_request_data("test_recipes_search_by_ingredients")
        recipe_search_by_ingredients_request_url = self.get_request_url(base_url, request_parameters)
        recipe_search_by_ingredients_reply = self.get_request(recipe_search_by_ingredients_request_url)

        assert recipe_search_by_ingredients_reply.status_code == 200
        json_recipe_search_by_ingredients_reply = recipe_search_by_ingredients_reply.json()
        assert len(json_recipe_search_by_ingredients_reply) > 0
        assert 'id' in json_recipe_search_by_ingredients_reply[0]
        assert 'title' in json_recipe_search_by_ingredients_reply[0]
        ingredients = request_parameters['ingredients'].split(',')
        for used_ingredient in json_recipe_search_by_ingredients_reply[0].get('usedIngredients'):
            present = False
            for ingredient_name in used_ingredient.get('name').split(' '):
                if ingredient_name in ingredients:
                    present = True
        assert present