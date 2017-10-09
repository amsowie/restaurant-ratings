

def get_ratings(filename, view=0):
    """Restaurant rating lister."""
    f = open(filename)
    ratings = {}

    for line in f:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        ratings[restaurant] = rating
    if view == "1":  
        ratings_list = sorted(ratings.items())
        for restaurant, rating in ratings_list:
            print '{} is rated at {}.'.format(restaurant, rating)

    return ratings

def add_rating(ratings):
    """
        add restaurant and rating
    """
    restaurant_score = 0

    restaurant_name = raw_input("Please enter a restaurant name: ").title()

    while restaurant_score < 1 or restaurant_score > 5:
        restaurant_score = int(raw_input("Please enter a rating score: "))
        if restaurant_score < 1:
            print "Your rating is too low."
        elif restaurant_score > 5:
            print "Your rating is too high."



    ratings[restaurant_name] = restaurant_score
    ratings_list = sorted(ratings.items())
    for restaurant, rating in ratings_list:
        print '{} is rated at {}.'.format(restaurant, rating)

    print


def user_choices(filename):
    """ Allows user to choose seeing ratings, adding restaurant, or quit"""
    user_choice = ""

    while user_choice != "q":
        print "Enter 1 to see the current ratings."
        print "Enter 2 to add a restaurant and value."
        print "Enter q to quit."
        user_choice = raw_input("Please choose one of the above: ")

        if user_choice == "1":
            get_ratings(filename,"1")
        elif user_choice == "2":
            add_rating(filename)
        elif user_choice == "q":
            break

if __name__ == '__main__':
    user_choices("scores.txt")


