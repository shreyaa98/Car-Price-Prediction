// Define data structures

const pizzaIngredients = {
  dough: ["flour", "water", "yeast", "salt"],
  sauce: ["tomatoes", "olive oil", "garlic", "basil"],
  toppings: ["cheese", "pepperoni", "mushrooms", "bell peppers"],
};

// Side-effect-free functions

const prepareDough = ingredients => ingredients.dough.join(", ");

const makeSauce = ingredients => ingredients.sauce.join(", ");

const addToppings = (base, toppings) => `${base} with ${toppings.join(", ")}`;

// Higher-order functions

const assemblePizza = (ingredientGetter, toppingAdder) => {
  const base = ingredientGetter(pizzaIngredients);
  const toppings = toppingAdder(pizzaIngredients.toppings);
  return `${base} and ${toppings}`;
};

// Functions as parameters and return values

const bakePizza = pizza => `Bake the ${pizza} in the oven until crust is golden.`;

// Closures / Anonymous functions

const servePizza = (() => {
  let slices = 8;
  
  return () => {
    if (slices > 0) {
      slices--;
      return `Enjoy a slice! ${slices} slices remaining.`;
    } else {
      return "No more pizza slices left.";
    }
  };
})();

// Example usage

const pizza = assemblePizza(prepareDough, toppings => addToppings(makeSauce(pizzaIngredients), toppings));
console.log(pizza);

const bakedPizza = bakePizza(pizza);
console.log(bakedPizza);

console.log(servePizza());
console.log(servePizza());
// ...
