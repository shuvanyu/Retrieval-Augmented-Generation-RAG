def get_base_prompt():
    
    return """You are tasked to answer user query based on the following context items.
    Give yourself room to think by extracting relevant passages from the context
    before answering the query. Don't return the thinking, only return the answer.
    Make sure your answers are as explanatory as possible.
    Use the following examples as reference for the ideal answer style. Even if the context items
    does not have the exact terms as that of the user query, you are free to infer
    what the user is trying to ask and then answer the query from the context items.

    \nExample 1:
    Query: How to make broccoli and cheddar soup?
    Answer: This is a recipe for broccoli and aged cheddar soup:

    Ingredients:
    1 large head of broccoli, chopped into florets
    1 medium onion, finely chopped
    2 cloves garlic, minced
    2 tablespoons butter
    2 tablespoons all-purpose flour
    4 cups vegetable or chicken broth
    1 cup heavy cream or half-and-half
    2 cups aged cheddar cheese, grated
    Salt and pepper to taste
    Optional: 1/2 teaspoon mustard powder or a dash of hot sauce for extra flavor

    Instructions:
    1. Rinse the broccoli thoroughly and chop it into small florets. Peel and chop the stem if desired.
    2. In a large pot, melt the butter over medium heat. Add the chopped onion and cook until it becomes translucent, about 5 minutes.
    3. Add the minced garlic and cook for another 1-2 minutes until fragrant.
    4. Sprinkle the flour over the onions and garlic, stirring constantly to form a roux. Cook for about 2 minutes to eliminate the raw flour taste.
    5. Gradually whisk in the broth, ensuring there are no lumps. Bring the mixture to a boil.
    6. Add the chopped broccoli to the pot. Reduce the heat to a simmer and cook until the broccoli is tender, about 10-15 minutes.
    7. Use an immersion blender to blend the soup until smooth. If you prefer a chunkier texture, blend only a portion of the soup.
    Alternatively, carefully transfer the soup in batches to a blender and blend until smooth. Return the blended soup to the pot.
    8. Stir in the heavy cream or half-and-half, and bring the soup back to a simmer.
    9. Gradually add the grated aged cheddar cheese, stirring constantly until it melts and the soup is smooth.
    10. Season with salt and pepper to taste. If using mustard powder or hot sauce, add it at this stage.
    11. Ladle the soup into bowls and serve hot. Garnish with additional grated cheddar, croutons, or a sprinkle of chopped chives if desired.
    
    \nExample 2:
    Query: How to roast vegetables?
    Answer: Here is the recipe below:
    Choose any combination of the following vegetables: 
    Ingredients:
    Parsnips 
    Carrots 
    Potatoes 
    Onions 
    Green beans (whole) 
    Turnips 
    Rutabagas 
    Winter Squash 
    Bell peppers 
    Whole garlic cloves 
    Eggplant 
    Asparagus 
    Beets 
    Sweet Potatoes 
    Broccoli 
    Cauliflower

    Instructions: 
    1. Preheat oven to 400°F.  
    2. Cut vegetables of your choice into large chunks, about 1” x 2”. 
    3. Oil a large roasting pan or baking sheet with 1-2 tbsp. olive oil. Add the cut vegetables and 
    salt and pepper to taste. Gently turn vegetables to coat with the olive oil, adding more oil if 
    desired. Add additional herbs or spices such as thyme, rosemary, sage, or cinnamon, cloves, 
    and nutmeg depending on the type of vegetables you are making. 
    4. Put the pan or baking sheet in the oven and roast the vegetables for 30-50 minutes, or until 
    they are tender and golden brown. Turn the vegetables with a spatula every 10 – 15 minutes. 
    5. Once finished, add more seasonings if needed and serve immediately.
    
    \nExample 3:
    Query: Vanilla-Peach Smoothie 
    Answer: Here are the steps below:
    Ingredients:
    2 cups yogurt 
    1 ½ cup orange juice, or as much as needed 
    ½ tsp vanilla extract 
    ½ frozen banana, optional 
    2 cups unsweetened frozen sliced or chopped peaches

    Instructions:
    1. Put the yogurt, juice, vanilla, and banana in the blender first, followed by the peaches. 
    2. Pulse blender to start, then turn on high to smooth. If the mixture is stiff, add more liquid. 
    Serve right away. 
    
    \nNow use the following context to answer the user query:
    {context}
    
    \nRelevant passages: <extract relevant passages from the context here>
    User query: {query}
    Answer:"""