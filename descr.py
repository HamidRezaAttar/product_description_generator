import random
from config import variations


class Descr:
    def __init__(self):
        pass

    def gen_description(
        self,
        name,
        price,
        brand,
        color,
        size,
        material,
        design,
        condition,
        rating,
        discount=0,
    ):
        description = f"Introducing the {name} from {brand}, available in {color} and made of {material}. "
        description += (
            f"This product is available in size {size} and features a {design} design. "
        )
        description += f"It is in {condition} condition and has received a rating of {rating} stars. "
        description += (
            f"Priced at only ${price}, it's a steal for such a high-quality product."
        )
        if discount > 0:
            price -= price * (discount / 100)
            description += f"\nAnd now with {discount}% off, it's only ${price}!"

        description += "\n" + random.choice(variations)

        return description

    def gen_description_preset(
        self,
        name,
        price,
        brand,
        color,
        size,
        material,
        design,
        condition,
        rating,
        discount=0,
        preset="default",
    ):
        description = f"Introducing the {name} from {brand}, available in {color} and made of {material}. "

        if preset == "default":
            description += f"This product is available in size {size} and features a {design} design. "
            description += f"It is in {condition} condition and has received a rating of {rating} stars. "
            description += f"Priced at only ${price}, it's a steal for such a high-quality product."
        elif preset == "brief":
            description += (
                f"It features a {design} design and is in {condition} condition. "
            )
            description += f"Priced at only ${price}, it's a great value for a high-quality product."
        elif preset == "detailed":
            description += f"This product is available in size {size} and features a {design} design. "
            description += f"It is in {condition} condition and has received a rating of {rating} stars. "
            description += f"Made of {material}, it's both stylish and practical. "
            description += f"Priced at only ${price}, it's a great value for such a high-quality product."
        elif preset == "luxury":
            description += f"This luxury product is available in size {size} and features a {design} design. "
            description += f"It is in {condition} condition and has received a rating of {rating} stars. "
            description += f"Made of top-quality {material}, it's the epitome of style and comfort. "
            description += f"Priced at only ${price}, it's a steal for a luxury product of this quality."

        if discount > 0:
            price -= price * (discount / 100)
            description += f"\nAnd now with {discount}% off, it's only ${price}!"

        description += "\n" + random.choice(variations)

        return description
