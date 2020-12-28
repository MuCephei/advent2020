magic_value = 20201227

def transform(x, n, magic):
    value = 1
    for _ in range(n):
        value *= x
        value = value % magic
    return value

def inverse_transform(target, x, magic, min=1):
    n = 1
    while target % x != 0 or target != x or n < min:
        while target % x != 0:
            target += magic
        target = target / x
        n += 1
    return n

def encryption_key(pub_key, loop_size):
    return transform(pub_key, loop_size, magic_value)

def next_possible_loop_size(start, pub_key):
    return inverse_transform(pub_key, 7, magic_value, start)

def hack(card_pub_key, door_pub_key):
    card_loop = 0
    door_loop = 0
    card_keys = {}
    door_keys = {}
    while True:
        card_loop_size = next_possible_loop_size(card_loop, card_pub_key)
        enc_key = encryption_key(door_pub_key, card_loop_size)
        if enc_key in door_keys:
            return enc_key
        card_keys[enc_key] = card_loop_size

        door_loop_size = next_possible_loop_size(door_loop, door_pub_key)
        enc_key = encryption_key(card_pub_key, door_loop_size)
        if enc_key in card_keys:
            return enc_key
        door_keys[enc_key] = door_loop_size

def parse_input():
    with open('input.txt', 'r') as file:
        card_pub_key = int(file.readline().strip("\n"))
        door_pub_key = int(file.readline().strip("\n"))
    return card_pub_key, door_pub_key

card_pub_key, door_pub_key = parse_input()
private_key = hack(card_pub_key, door_pub_key)
print(private_key)


