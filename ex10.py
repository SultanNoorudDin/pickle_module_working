import pickle

data_set = "data.pkl"
file_object = open(data_set, "rb")
real_data = pickle.load(file_object)
print(real_data)


data = open("irisdata.txt", "r+")
file = data.read().splitlines()
with open("data.pkl","wb") as file_obj:
    # file_obj = open(file, "wb")
    pickle.dump(file, file_obj)
file_obj.close()