from backpack_loader import BackpackLoader

def main():
    meal_list_file = "elf_meal_list.txt"
    backpack_loader = BackpackLoader(meal_list_file)
    backpacks = backpack_loader.generate_backpack()

    sorted_backpacks = [backpack.total_value() for backpack in backpacks]
    sorted_backpacks.sort(reverse=True)

    print(f"Largest backpack calories:= {max(sorted_backpacks)}")

    top_three_backpacks = sorted_backpacks[0:3]

    print(f"Largest three backpacks:= {top_three_backpacks} {sum(top_three_backpacks)}")


if __name__ == "__main__":
    main()

