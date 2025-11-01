from __builtins__ import *


def get_random_hat():
    hats_list = [
        Hats.Cactus_Hat,
        Hats.Carrot_Hat,
        Hats.Gold_Hat,
        Hats.Golden_Cactus_Hat,
        Hats.Golden_Sunflower_Hat,
        Hats.Pumpkin_Hat,
        Hats.Sunflower_Hat,
        Hats.Traffic_Cone,
        Hats.Tree_Hat,
        Hats.Wizard_Hat
    ]

    return hats_list[random() * len(hats_list) // 1]


def main():
    clear()
    get_random_hat()
    change_hat(get_random_hat())


if __name__ == "__main__":
    main()
