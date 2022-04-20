from utils import SpoonacularTests


class TestRecipesById(SpoonacularTests):
    
    def test_recipes_taste_by_id(self):
        base_url, request_parameters = self.get_request_data("test_recipes_taste_by_id")
        recipe_taste_by_id_request_url = self.get_request_url(base_url, request_parameters)
        recipe_taste_by_id_reply = self.get_request(recipe_taste_by_id_request_url)

        assert recipe_taste_by_id_reply.status_code == 200
        json_recipe_taste_by_id_reply = recipe_taste_by_id_reply.json()
        assert 'sweetness' in json_recipe_taste_by_id_reply
        assert 'saltiness' in json_recipe_taste_by_id_reply
        assert 'sourness' in json_recipe_taste_by_id_reply
        assert 'bitterness' in json_recipe_taste_by_id_reply
        assert 'savoriness' in json_recipe_taste_by_id_reply
        assert 'fattiness' in json_recipe_taste_by_id_reply
        assert 'spiciness' in json_recipe_taste_by_id_reply

    def test_recipes_equipment_by_id(self):
        base_url, request_parameters = self.get_request_data("test_recipes_equipment_by_id")
        recipe_equipment_by_id_request_url = self.get_request_url(base_url, request_parameters)
        recipe_equipment_by_id_reply = self.get_request(recipe_equipment_by_id_request_url)

        assert recipe_equipment_by_id_reply.status_code == 200
        json_recipe_equipment_by_id_reply = recipe_equipment_by_id_reply.json()
        assert len(json_recipe_equipment_by_id_reply.get('equipment')) > 0

    def test_recipes_price_breakdown_by_id(self):
        base_url, request_parameters = self.get_request_data("test_recipes_price_breakdown_by_id")
        recipe_price_breakdown_by_id_request_url = self.get_request_url(base_url, request_parameters)
        recipe_price_breakdown_by_id_reply = self.get_request(recipe_price_breakdown_by_id_request_url)

        assert recipe_price_breakdown_by_id_reply.status_code == 200
        json_recipe_price_breakdown_by_id_reply = recipe_price_breakdown_by_id_reply.json()
        assert 'ingredients' in json_recipe_price_breakdown_by_id_reply
        assert 'totalCost' in json_recipe_price_breakdown_by_id_reply
        assert 'totalCostPerServing' in json_recipe_price_breakdown_by_id_reply

    def test_recipes_ingredients_by_id(self):
        base_url, request_parameters = self.get_request_data("test_recipes_ingredients_by_id")
        recipe_ingredients_by_id_request_url = self.get_request_url(base_url, request_parameters)
        recipe_ingredients_by_id_reply = self.get_request(recipe_ingredients_by_id_request_url)

        assert recipe_ingredients_by_id_reply.status_code == 200
        json_recipe_ingredients_by_id_reply = recipe_ingredients_by_id_reply.json()
        assert len(json_recipe_ingredients_by_id_reply.get('ingredients'))

    def test_recipes_nutrition_by_id(self):
        base_url, request_parameters = self.get_request_data("test_recipes_nutrition_by_id")
        recipe_nutrition_by_id_request_url = self.get_request_url(base_url, request_parameters)
        recipe_nutrition_by_id_reply = self.get_request(recipe_nutrition_by_id_request_url)

        assert recipe_nutrition_by_id_reply.status_code == 200
        json_recipe_nutrition_by_id_reply = recipe_nutrition_by_id_reply.json()
        assert 'calories' in json_recipe_nutrition_by_id_reply
        assert 'carbs' in json_recipe_nutrition_by_id_reply
        assert 'fat' in json_recipe_nutrition_by_id_reply
        assert 'protein' in json_recipe_nutrition_by_id_reply
