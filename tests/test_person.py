import pytest
from viewing_party.person import Person

# def __init__(self, name, watched, friends, subscriptions):
#         self.name = name
#         self.watched = watched
#         self.friends = friends
#         self.subscriptions = subscriptions

#     def add_watched(self, movie):
#         self.watched.append(movie)
#         return self.watched
    
#     def get_num_watched(self):
#         return len(self.watched)
def test_1_create_person_valid_inputs():
    # Arrange and Act
    person1 = Person("Cheetah",["Titanic", "Top Gun"], ["Lion", "Tiger"], ["Hulu", "HBX", "Netflix"])

    # Assert
    assert person1.name == "Cheetah"
    assert person1.watched == ["Titanic", "Top Gun"]
    assert person1.friends == ["Lion", "Tiger"]
    assert person1.subscriptions == ["Hulu", "HBX", "Netflix"]
    

