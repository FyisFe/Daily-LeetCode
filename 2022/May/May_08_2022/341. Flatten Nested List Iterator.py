class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        def get(currList: List[NestedInteger]) -> Generator[int, None, None]:
            """
            Generator function to iterate through all nested NestedInteger objects and return its integer value.
            :param currList: The current (nested) list of NestedIntegers to iterate through.
            :yields:         The integer value of the current NestedInteger in the iteration.
            """
            for nestedInteger in currList:
                if (
                    nestedInteger.isInteger()
                ):  # nestedInteger has a single integer value
                    yield nestedInteger.getInteger()
                else:  # nestedInteger is a list of NestedIntegers
                    yield from get(nestedInteger.getList())

        self.generator = get(
            nestedList
        )  # Initialise the generator object with the given NestedInteger list
        self.nextInteger = next(
            self.generator, None
        )  # Obtain the next (first) NestedInteger pre-emptively

    def next(self) -> int:
        result = self.nextInteger  # store the current NestedInteger integer value
        self.nextInteger = next(
            self.generator, None
        )  # Obtain the next NestedInteger pre-emptively
        return result

    def hasNext(self) -> bool:
        return self.nextInteger is not None
