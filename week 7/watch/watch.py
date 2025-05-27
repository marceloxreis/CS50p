import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'<iframe src="https?:\/\/(?:www\.)?youtube\.com/embed/(\w+)', s)
    if match:
        video_id = match.group(1)
        # Replace embed link with regular YouTube or youtu.be link
        return f'https://youtu.be/{video_id}'  # You can also return the shortened version with youtu.be
    else:
        return "None"

if __name__ == "__main__":
    main()
