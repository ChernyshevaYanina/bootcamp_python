def find_m_pattern(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        if len(lines) != 3 or len(lines[0].strip()) != 5:
            return 'False'
        
        if lines[0].strip()[0] == '*' and \
            lines[0].strip()[4] == '*' and \
            lines[1].strip()[0] == '*' and \
            lines[1].strip()[1] == '*' and \
            lines[1].strip()[3] == '*' and \
            lines[1].strip()[4] == '*' and \
            lines[2].strip()[0] == '*' and \
            lines[2].strip()[2] == '*' and \
            lines[2].strip()[4] == '*':
            counting = 0
            for line in lines:
                counting += line.count('*')
            if counting == 9:
                return 'True'
            else:
                return 'False'
        else:
            return 'False'

def main():
    print(find_m_pattern("m.txt"))

if __name__ == "__main__":
    main()

