class Dog:

    def eat(**kwargs):
        return "Eating.." + kwargs['name']

    def bark():
        return "Barking.."

    def run():
        return "Running.."

    def sleeping():
        return "Sleeping.."

# class Cat:

#     def eat():
#         return "Eating.."

#     def bark():
#         return "Barking.."

#     def run():
#         return "Running.."

#     def sleeping():
#         return "Sleeping.."

if __name__ == "__main__":

    dg = Dog
    action = dg.eat(name = "Saver")
    print (action)

    # ct = Cat
    # action = ct.eat(name = "Tom")
    # print (action)