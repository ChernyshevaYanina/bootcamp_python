import argparse

def decypher(text):
    words = text.split()
    first_letters = [word[0] for word in words]
    return ''.join(first_letters)

def main():
    parser = argparse.ArgumentParser(description='Расшифровка текста')
    parser.add_argument('text', type=str, help='Текст для расшифровки')
    args = parser.parse_args()

    decrypted_text = decypher(args.text)
    print(decrypted_text)

if __name__ == '__main__':
    main()