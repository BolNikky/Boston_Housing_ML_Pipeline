import pickle
 
# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
 
# Print the type
print(type(model))