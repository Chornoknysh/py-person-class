class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age!r})"


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    instances: list[Person] = []

    for data in people:
        person = Person(name=data["name"], age=data["age"])
        instances.append(person)

    for data in people:
        current = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            current.wife = Person.people[data["wife"]]

        if "husband" in data and data["husband"] is not None:
            current.husband = Person.people[data["husband"]]

    return instances
