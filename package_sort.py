def sort(width: int, height: int, length: int, mass: int) -> str:
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def test_standard() -> None:
    print(f"test_standard {sort (50, 50, 50, 10)}")

def test_special_bulky_not_heavy() -> None:
    print(f"test_special_bulky_not_heavy {sort (200, 200, 200, 10)}")

def test_special_heavy_not_bulky() -> None:
    print(f"test_special_heavy_not_bulky {sort (50, 50, 50, 25)}")

def test_rejected_both_bulky_and_heavy() -> None:
    print(f"test_rejected_both_bulky_and_heavy {sort (200, 200, 200, 50)}")

def test_standard_neither_bulky_nor_heavy() -> None:
    print(f"test_standard_neither_bulky_nor_heavy {sort (50, 50, 50, 10)}")

test_standard()
test_special_bulky_not_heavy()
test_special_heavy_not_bulky()
test_rejected_both_bulky_and_heavy()
test_standard_neither_bulky_nor_heavy()
