import art

art.show_art()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    cypher_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_index = alphabet.index(letter) + shift_amount
            shifted_index %= len(alphabet)
            cypher_text += alphabet[shifted_index]
        else:
            cypher_text += letter

    print(f"Here is the {encode_or_decode}d result: {cypher_text}")


should_continue = True

while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(message, shift, direction)

    restart_answer = input("\nDo you want to go again? [yes/no]: ").lower()
    if restart_answer != "yes":
        should_continue = False
        print("\nGoodbye!")
